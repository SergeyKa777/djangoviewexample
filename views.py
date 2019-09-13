from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import math
import cmath
from .forms import *
from sympy import *
from decimal import Decimal
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from ggg.models import Money
import dateutil.parser
import hashlib
from sympy.solvers import solve
from sympy import Symbol
from scipy import integrate
from sympy import limit, tan, cos, cot, Symbol, oo, acos, acot, atan, sin, sqrt, exp, log, pi
from sympy.abc import x
from scipy.misc import derivative
import numexpr as ne
import numpy
import wolframalpha
import ast
from ggg.price import *


def floint(digit):
    if digit == int(digit):
        digit = int(digit)
    else:
        digit = float(digit)
    return digit

naeb = "Тот самый момент когда не получилось обмануть ))"
m0 = 1.2566371 * 10 ** -6


def proverka(requestuser):
    zzzzzzz = Money.objects.filter(moneyname=requestuser)
    for fffffff in zzzzzzz:
        jj = fffffff.moneyvalue
    return jj


def razrabotka(request):
    global math_zad
    zzzzzzz = Money.objects.filter(moneyname=request.user)
    for fffffff in zzzzzzz:
        jj = fffffff.moneyvalue
    return render(request, "razrabotka.html", {"jj": jj, "math_zad": math_zad})


# @login_required(login_url='/')
def test(request):
    if request.POST:
        form = Test(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            fns = cd['fns']
            cont = fns
            cont = fns.replace("**", "^")
            # moss = Money.objects.get(moneyname=request.user)
            # moss.moneyvalue -= fiz_zad
            # moss.save()
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue

            return render(request, "test.html", {"form": form, "cont": cont, "jj": jj, "fiz_zad": fiz_zad})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Test()
    return render(request, "test.html", {"form": form, "jj": jj, "fiz_zad": fiz_zad})


# @login_required(login_url='/')
def limits1(request):
    if request.POST:
        form = Limits1(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            fn = cd['fn']
            Lim1 = cd['Lim1']
            Lim2 = cd['Lim2']
            cont = limit(fn, Lim1, Lim2)
            # moss = Money.objects.get(moneyname=request.user)
            # moss.moneyvalue -= fiz_zad
            # moss.save()
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "mat1/limits1.html", {"form": form, "cont": cont, "jj": jj, "fiz_zad": fiz_zad})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Limits1()
    return render(request, "mat1/limits1.html", {"form": form, "jj": jj, "fiz_zad": fiz_zad})


################################################# MATH 1  START

@csrf_exempt
def math1_1_1(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            ss1 = request.POST['A']
            try:
                bb = np.array(ast.literal_eval(ss1), dtype='float32')
                pp = np.linalg.det(bb)
                if pp == int(pp):
                    pp = int(pp)
                else:
                    pp = pp
                sss = "`" + str(pp) + "`"

            except Exception:
                sss = "Ошибка вычисления,определитель можно вычислить только для квадратной матрицы!!!"
            finally:
                try:
                    bb1 = np.array(ast.literal_eval(ss1))  # Конвертировать Str(массив в массив nympy)
                    bbb = bb1.transpose()
                    bbb = bbb.tolist()  # Преобразовать массив NumPy в список с разделителем ,
                    bbb = str(bbb)
                    bb2 = np.array(ast.literal_eval(ss1))
                    bbb1 = np.linalg.inv(bb2)
                    bbb1 = bbb1.tolist()  # Преобразовать массив NumPy в список с разделителем ,
                    bbb1 = str(bbb1)
                except Exception:
                    bbb1 = "`Ошибка вычисления,инвертированная матрица может быть только квадратной!!!`"

            moss = Money.objects.get(moneyname=request.user)
            moss.moneyvalue -= math_zad
            moss.save()
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa, 'bbb': bbb, 'bbb1': bbb1}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_1_1()
        return render(request, "mat1/math1_1_1.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_1_2(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            ss1 = request.POST['A']
            x1 = Symbol("x1")
            x2 = Symbol("x2")
            x3 = Symbol("x3")
            x4 = Symbol("x4")
            x5 = Symbol("x5")
            gg = sympify(ss1)
            try:
                system = Matrix(gg)
                bb = solve_linear_system(system, x1, x2, x3, x4, x5)
                sss = str(bb)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception:
                sss = "Ошибка вычисления,определитель можно вычислить только для квадратной матрицы!!!"
                system = Matrix(gg)
                bb = solve_linear_system(system, x1, x2, x3, x4, x5)
                sss = str(type(bb))

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_1_2()
        return render(request, "mat1/math1_1_2.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_1_3(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            ss1 = request.POST['A']
            ss2 = request.POST['B']
            ss3 = request.POST['C']
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                bb1 = ast.literal_eval(ss1)
                bb2 = ast.literal_eval(ss2)
                A = np.array(bb1)
                B = np.array(bb2)
                if np.shape(A) != np.shape(B):
                    sss = np.dot(B, A)
                    sss = np.array2string(sss, precision=2, separator=',', suppress_small=True)
                elif np.shape(A) == np.shape(B):
                    sss = ne.evaluate(ss3)
                    sss = np.array2string(sss, precision=2, separator=',', suppress_small=True)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = ff
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_1_3()
        return render(request, "mat1/math1_1_3.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_1_4(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            ss1 = request.POST['A']
            x1 = Symbol("x1")
            x2 = Symbol("x2")
            x3 = Symbol("x3")
            x4 = Symbol("x4")
            x5 = Symbol("x5")
            A = sympify(ss1)
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                gg = sympify(A)
                print(len(gg[0]))
                varcount = len(gg[0]) - 1
                system = Matrix(gg)
                bb = solve_linear_system(system, x1, x2, x3, x4, x5)
                if bb == None:
                    sss = "Матрица несовместная (не имеет решений)"
                elif varcount == len(bb):
                    sss = "Матрица совместная и определенная (имеет единственное решение)"
                else:
                    sss = "Матрица совместная и неопределенная (имеет бесконечно много решений)"
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = ff

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_1_4()
        return render(request, "mat1/math1_1_4.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_1_5(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            a = request.POST['A']
            b = request.POST['B']
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = a.split("x")
                b = b.split("x")
                if b[1] == a[0]:
                    sss = "`" + b[0] + "x" + a[1] + "`"
                    moss = Money.objects.get(moneyname=request.user)
                    moss.moneyvalue -= math_zad
                    moss.save()
                elif b[1] != a[0]:
                    sss = "Данные матрицы умножать нельзя"
                    moss = Money.objects.get(moneyname=request.user)
                    moss.moneyvalue -= math_zad
                    moss.save()
                else:
                    sss = "Что то пошло не по плану !!!"
            except Exception as err:
                err = str(err)
                sss = "System Error:" + err
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_1_5()
        return render(request, "mat1/math1_1_5.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_1_6(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                c = request.POST['C']

                a = a.split("x")
                b = b.split("x")
                c = c.split("x")

                arra = np.ones((int(a[0]), int(a[1])), dtype=np.int8)
                arrb = np.ones((int(b[0]), int(b[1])), dtype=np.int8)
                arrc = np.ones((int(c[0]), int(c[1])), dtype=np.int8)

                def func1(arra, arrb, arrc):
                    try:
                        arra = arra.transpose()
                        razma = np.shape(arra)
                        razmb = np.shape(arrb)
                        razmc = np.shape(arrc)
                        if razmc[1] == razmb[0] and razmb[1] == razma[0]:
                            sss = "`C*B*A^t` - ИСТИНА"
                        else:
                            sss = "`C*B*A^t` - ЛОЖЬ"
                    except Exception as err:
                        sss = "Фунция не работает 1"
                        print(err)
                        print("--------------")
                    return sss

                ############################
                def func2(arra, arrb, arrc):
                    try:
                        arrc = arrc.transpose()
                        razma = np.shape(arra)
                        razmb = np.shape(arrb)
                        razmc = np.shape(arrc)
                        if razma[1] == razmc[0]:
                            sss = "`A*C^t` - ИСТИНА"
                        else:
                            sss = "`A*C^t` - ЛОЖЬ"
                    except Exception as err:
                        sss = "Фунция не работает 2"
                        print(err)
                        print("--------------")
                    return sss

                #####################
                def func3(arra, arrb, arrc):
                    try:
                        razma = np.shape(arra)
                        razmb = np.shape(arrb)
                        razmc = np.shape(arrc)
                        if razma[1] == razmb[0] and razmb[1] == razmc[0]:
                            sss = "`A*B*C` - ИСТИНА"
                        else:
                            sss = "`A*B*C` - ЛОЖЬ"
                    except Exception as err:
                        sss = "Фунция не работает 3"
                        print(err)
                        print("--------------")
                    return sss

                #####################
                def func4(arra, arrb, arrc):
                    try:
                        razma = np.shape(arra)
                        razmb = np.shape(arrb)
                        razmc = np.shape(arrc)
                        if razmc[1] == razmb[0]:
                            sss = "`C*B` - ИСТИНА"
                        else:
                            sss = "`C*B` - ЛОЖЬ"
                    except Exception as err:
                        sss = "Фунция не работает 4"
                        print(err)
                        print("--------------")
                    return sss

                #####################
                def func5(arra, arrb, arrc):
                    try:
                        arra = arra.transpose()
                        razma = np.shape(arra)
                        razmb = np.shape(arrb)
                        razmc = np.shape(arrc)
                        if razmc[1] == razma[0] and razma[1] == razmb[0]:
                            sss = "`C*A^t*B` - ИСТИНА"
                        else:
                            sss = "`C*A^t*B` - ЛОЖЬ"
                    except Exception as err:
                        sss = "Фунция не работает 5"
                        print(err)
                        print("--------------")
                    return sss

                #####################
                def func6(arra, arrb, arrc):
                    try:
                        pp = np.shape(arrb)
                        if pp[0] == pp[1]:
                            sss = True
                            sss = "`B^2` - ИСТИНА"
                        else:
                            sss = False
                            sss = "`B^2` - ЛОЖЬ"

                    except Exception as err:
                        sss = "Фунция не работает 6"
                        print(err)
                        print("--------------")
                    return sss

                #####################
                def func7(arra, arrb, arrc):
                    try:
                        razma = np.shape(arra)
                        razmb = np.shape(arrb)
                        razmc = np.shape(arrc)
                        if razmc[1] == razma[0]:
                            sss = "`C*A` - ИСТИНА"
                        else:
                            sss = "`C*A` - ЛОЖЬ"
                    except Exception as err:
                        sss = "Фунция не работает 7"
                        print(err)
                        print("--------------")
                    return sss

                a1 = func1(arra, arrb, arrc)
                a2 = func2(arra, arrb, arrc)
                a3 = func3(arra, arrb, arrc)
                a4 = func4(arra, arrb, arrc)
                a5 = func5(arra, arrb, arrc)
                a6 = func6(arra, arrb, arrc)
                a7 = func7(arra, arrb, arrc)
                sss = {"x1": a1, "x2": a2, "x3": a3, "x4": a4, "x5": a5, "x6": a6, "x7": a7}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
                zzzzzzz = Money.objects.filter(moneyname=request.user)
                for fffffff in zzzzzzz:
                    jj = fffffff.moneyvalue
                aa = str(request.user)
                return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
                return JsonResponse(return_object)
            except Exception:
                zzzzzzz = Money.objects.filter(moneyname=request.user)
                for fffffff in zzzzzzz:
                    jj = fffffff.moneyvalue
                aa = str(request.user)
                sss = {"x1": "Ошибка вычислений !!!"}
                return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
                return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_1_6()
        return render(request, "mat1/math1_1_6.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_1(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                c = request.POST['C']
                x = Symbol("x")
                y = Symbol("y")
                z = Symbol("z")
                arra = np.array(ast.literal_eval(a))
                arrb = np.array(ast.literal_eval(b))
                arrc = np.array(ast.literal_eval(c))
                ab = arrb - arra
                a1 = ab[0]
                a2 = ab[1]
                a3 = ab[2]
                b1 = arrc[0]
                b2 = arrc[1]
                b3 = arrc[2]
                x = solve(b1 - x - a1, x)
                y = solve(b2 - y - a2, y)
                z = solve(b3 - z - a3, z)
                ff = tuple(x + y + z)
                ff = str(ff)
                sss = {"ff": ff}
                # sss="pizdec"
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_1()
        return render(request, "mat1/math1_2_1.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_2(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                c = request.POST['C']
                arra = np.array(ast.literal_eval(a))
                arrb = np.array(ast.literal_eval(b))
                arrc = np.array(ast.literal_eval(c))
                xc = (arra[0] + arrb[0] + arrc[0]) / 3
                yc = (arra[1] + arrb[1] + arrc[1]) / 3
                zc = (arra[2] + arrb[2] + arrc[2]) / 3
                if xc / int(xc) == 1:
                    xc = int(xc)
                else:
                    xc = xc
                if yc / int(yc) == 1:
                    yc = int(yc)
                else:
                    yc = yc
                if zc / int(zc) == 1:
                    zc = int(zc)
                else:
                    zc = zc

                xc = round(xc, 5)
                yc = round(yc, 5)
                zc = round(zc, 5)
                ff = (xc, yc, zc)
                ff = str(ff)
                sss = {'ff': ff}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_2()
        return render(request, "mat1/math1_2_2.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_3(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                c = request.POST['C']
                arra = np.array(ast.literal_eval(a))
                arrb = np.array(ast.literal_eval(b))
                arrc = np.array(ast.literal_eval(c))
                aaa = abs(np.dot(arra, np.cross(arrc, arrb)))
                ff = str(aaa)

                sss = {'ff': ff}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_3()
        return render(request, "mat1/math1_2_3.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_4(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                c = request.POST['C']
                arra = np.array(ast.literal_eval(a), dtype='float32')
                arrb = np.array(ast.literal_eval(b), dtype='float32')
                arrc = np.array(ast.literal_eval(c), dtype='float32')

                def func1(arra, arrb, arrc):
                    a = np.dot(arra, np.cross(arrb, arrc))
                    if a == 0:
                        sss = "Векторы компланарны."
                    else:
                        sss = "Векторы не компланарны."
                    return sss

                def func2(arra, arrb, arrc):
                    u1 = arra[0] / arrb[0]
                    u2 = arra[1] / arrb[1]
                    u3 = arra[2] / arrb[2]
                    u4 = arra[0] / arrc[0]
                    u5 = arra[1] / arrc[1]
                    u6 = arra[2] / arrc[2]
                    u7 = arrc[0] / arrb[0]
                    u8 = arrc[1] / arrb[1]
                    u9 = arrc[2] / arrb[2]
                    if u1 == u2 == u3 or u4 == u5 == u6 or u7 == u8 == u9:
                        sss = "Среди этих векторов есть коллинеарные."
                    else:
                        sss = "Среди этих векторов нет коллинеарныx."
                    return sss

                def func3(arra, arrb, arrc):
                    gg = np.concatenate([[arra], [arrb], [arrc]])
                    gg = np.linalg.det(gg)
                    if gg == 0:
                        sss = "Векторы линейно зависимы, и ориентация тройки не определяется."
                    elif gg > 0:
                        sss = "Векторы образуют правую тройку."
                    else:
                        sss = "Векторы образуют левую тройку."
                    return sss

                def func4(arra, arrb, arrc):
                    gg = np.concatenate([[arra], [arrb], [arrc]])
                    gg = gg.transpose()
                    gg = np.linalg.det(gg)
                    if gg != 0:
                        sss = "Векторы образуют базис в пространстве."

                    else:
                        sss = "Векторы не образуют базис в пространстве."
                    return sss

                a1 = func1(arra, arrb, arrc)
                a2 = func2(arra, arrb, arrc)
                a3 = func3(arra, arrb, arrc)
                a4 = func4(arra, arrb, arrc)
                sss = {"x1": a1, "x2": a2, "x3": a3, "x4": a4}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'x1': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_4()
        return render(request, "mat1/math1_2_4.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_5(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                c = request.POST['C']
                aa = sympify(a)
                bb = sympify(b)
                cc = sympify(c)
                x1 = aa[0]
                y1 = aa[1]
                z1 = aa[2]
                x2 = bb[0]
                y2 = bb[1]
                z2 = bb[2]
                x3 = cc[0]
                y3 = cc[1]
                z3 = cc[2]
                a = Symbol('a')
                u = solve(x1 * y2 * z3 + y1 * z2 * x3 + x2 * y3 * z1 - x3 * y2 * z1 - y1 * x2 * z3 - x1 * z2 * y3, a)
                u = u[0]
                if u == int(u):
                    u = int(u)
                else:
                    u = float(u)
                sss = {'ff': u}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_5()
        return render(request, "mat1/math1_2_5.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_6(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                aa = sympify(a)
                bb = sympify(b)
                x1 = aa[0]
                y1 = aa[1]
                z1 = aa[2]
                x2 = bb[0]
                y2 = bb[1]
                z2 = bb[2]
                a = Symbol('a')
                u = solve(x1 * x2 + y1 * y2 + z1 * z2, a)
                u = u[0]
                if u == int(u):
                    u = int(u)
                else:
                    u = float(u)
                sss = {'ff': u}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_6()
        return render(request, "mat1/math1_2_6.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_7(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                aa = sympify(a)
                bb = sympify(b)
                ax = aa[0]
                ay = aa[1]
                az = aa[2]
                bx = bb[0]
                by = bb[1]
                bz = bb[2]
                a = Symbol('a')
                b = Symbol('b')
                fun1 = ay * bz - az * by
                fun2 = ax * bz - az * bx
                fun3 = ax * by - ay * bx
                u1 = solve(fun1, a)
                u2 = solve(fun2, a)
                u3 = solve(fun3, a)
                u4 = solve(fun1, b)
                u5 = solve(fun2, b)
                u6 = solve(fun3, b)
                if not u1:
                    u1.append('w')
                if not u2:
                    u2.append('w')
                if not u3:
                    u3.append('w')
                if not u4:
                    u4.append('w')
                if not u5:
                    u5.append('w')
                if not u6:
                    u6.append('w')
                hh1 = u1[0]
                hh2 = u2[0]
                hh3 = u3[0]
                hh4 = u4[0]
                hh5 = u5[0]
                hh6 = u6[0]
                if type(hh1) is Symbol or type(hh1) is str or type(hh1) is Mul:
                    print("1")
                else:
                    aa = float(hh1)
                if type(hh2) is Symbol or type(hh2) is str or type(hh2) is Mul:
                    print("2")
                else:
                    aa = float(hh2)
                if type(hh3) is Symbol or type(hh3) is str or type(hh3) is Mul:
                    print("3")
                else:
                    aa = float(hh3)
                if type(hh4) is Symbol or type(hh4) is str or type(hh4) is Mul:
                    print("4")
                else:
                    bb = float(hh4)
                if type(hh5) is Symbol or type(hh5) is str or type(hh5) is Mul:
                    print("5")
                else:
                    bb = float(hh5)
                if type(hh6) is Symbol or type(hh6) is str or type(hh6) is Mul:
                    print("6")
                else:
                    bb = float(hh6)

                if aa == int(aa):
                    aa = int(aa)
                else:
                    aa = float(aa)
                if bb == int(bb):
                    bb = int(bb)
                else:
                    bb = float(bb)
                sss = {'a': aa, 'b': bb}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_7()
        return render(request, "mat1/math1_2_7.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_8(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']

                aa = sympify(a)
                bb = sympify(b)
                ax = aa[0]
                ay = aa[1]
                az = aa[2]
                bx = bb[0]
                by = bb[1]
                bz = bb[2]
                xx = bx - ax
                yy = by - ay
                zz = bz - az
                if xx == int(xx):
                    xx = int(xx)
                else:
                    xx = float(xx)
                if yy == int(yy):
                    yy = int(yy)
                else:
                    yy = float(yy)
                if zz == int(zz):
                    zz = int(zz)
                else:
                    zz = float(zz)
                sss = {'a_x': xx, 'a_y': yy, 'a_z': zz}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_8()
        return render(request, "mat1/math1_2_8.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_9(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                c = request.POST['C']

                bb1 = ast.literal_eval(a)
                bb2 = ast.literal_eval(b)
                a = np.array(bb1)
                b = np.array(bb2)
                sss = ne.evaluate(c)

                xx = sss[0]
                yy = sss[1]
                zz = sss[2]

                if xx == int(xx):
                    xx = int(xx)
                else:
                    xx = float(xx)
                if yy == int(yy):
                    yy = int(yy)
                else:
                    yy = float(yy)
                if zz == int(zz):
                    zz = int(zz)
                else:
                    zz = float(zz)
                sss = {'a_x': xx, 'a_y': yy, 'a_z': zz}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_9()
        return render(request, "mat1/math1_2_9.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_10(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']
                c = request.POST['C']
                c = ne.evaluate(c)
                bb1 = ast.literal_eval(a)
                bb2 = ast.literal_eval(b)
                a = np.array(bb1)
                b = np.array(bb2)
                ax = a[0]
                ay = a[1]
                az = a[2]
                bx = b[0]
                by = b[1]
                bz = b[2]
                xx = (ax + c * bx) / (1 + c)
                yy = (ay + c * by) / (1 + c)
                zz = (az + c * bz) / (1 + c)
                if xx == int(xx):
                    xx = int(xx)
                else:
                    xx = round(float(xx), 2)
                if yy == int(yy):
                    yy = int(yy)
                else:
                    yy = round(float(yy), 2)
                if zz == int(zz):
                    zz = int(zz)
                else:
                    zz = round(float(zz), 2)
                sss = {'M_x': xx, 'M_y': yy, 'M_z': zz}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_10()
        return render(request, "mat1/math1_2_10.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_11(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']

                bb1 = ast.literal_eval(a)
                bb2 = ast.literal_eval(b)
                a = np.array(bb1)
                b = np.array(bb2)
                ax = a[0]
                ay = a[1]
                az = a[2]
                bx = b[0]
                by = b[1]
                bz = b[2]
                xx = (np.dot(a, b)) / (
                        (math.sqrt(ax ** 2 + ay ** 2 + az ** 2)) * (math.sqrt(bx ** 2 + by ** 2 + bz ** 2)))
                if xx == int(xx):
                    xx = int(xx)
                else:
                    xx = round(float(xx), 6)
                sss = {'cos': xx}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_11()
        return render(request, "mat1/math1_2_11.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_12(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                b = request.POST['B']

                bb1 = ast.literal_eval(a)
                bb2 = ast.literal_eval(b)
                a = np.array(bb1)
                b = np.array(bb2)
                vv = np.cross(a, b)
                ax = vv[0]
                ay = vv[1]
                az = vv[2]
                xx = math.sqrt(ax ** 2 + ay ** 2 + az ** 2)
                if xx == int(xx):
                    xx = int(xx)
                else:
                    xx = round(float(xx), 6)
                sss = {'cos': xx}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_12()
        return render(request, "mat1/math1_2_12.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_13(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                bb1 = ast.literal_eval(a)
                a = np.array(bb1)
                ax = a[0]
                ay = a[1]
                az = a[2]
                xx = math.sqrt(ax ** 2 + ay ** 2 + az ** 2)
                if xx == int(xx):
                    xx = int(xx)
                else:
                    xx = round(float(xx), 6)
                sss = {'cos': xx}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_13()
        return render(request, "mat1/math1_2_13.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_14(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']
                bb1 = ast.literal_eval(a)
                a = np.array(bb1)
                ax = a[0]
                ay = a[1]
                az = a[2]
                xx = ax / math.sqrt(ax ** 2 + ay ** 2 + az ** 2)
                yy = ay / math.sqrt(ax ** 2 + ay ** 2 + az ** 2)
                zz = az / math.sqrt(ax ** 2 + ay ** 2 + az ** 2)
                if xx == int(xx):
                    xx = int(xx)
                else:
                    xx = round(float(xx), 4)
                if yy == int(yy):
                    yy = int(yy)
                else:
                    yy = round(float(yy), 4)
                if zz == int(zz):
                    zz = int(zz)
                else:
                    zz = round(float(zz), 4)
                sss = {'cosalpha': xx, 'cosbeta': yy, 'cosgamma': zz}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_14()
        return render(request, "mat1/math1_2_14.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_2_15(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['A']

                bb1 = ast.literal_eval(a)
                a = np.array(bb1)
                ax = a[0]
                ay = a[1]
                az = a[2]

                def fu1(ax, ay, az):
                    if ax != 0 and ay == 0 and az == 0:
                        print("a||ox")
                        ss = "a||ox"
                    else:
                        ss = ""
                    return ss

                def fu2(ax, ay, az):
                    if ay != 0 and ax == 0 and az == 0:
                        print("a||oy")
                        ss = "a||oy"
                    else:
                        ss = ""
                    return ss

                def fu3(ax, ay, az):
                    if az != 0 and ax == 0 and ay == 0:
                        print("a||oz")
                        ss = "a||oz"
                    else:
                        ss = ""
                    return ss

                def fu4(ax, ay, az):
                    if ax == 0:
                        print("a_|_ox")
                        ss = "a_|_ox"
                    else:
                        ss = ""
                    return ss

                def fu5(ax, ay, az):
                    if ay == 0:
                        print("a_|_oy")
                        ss = "a_|_oy"
                    else:
                        ss = ""
                    return ss

                def fu6(ax, ay, az):
                    if az == 0:
                        print("a_|_oz")
                        ss = "a_|_oz"
                    else:
                        ss = ""
                    return ss

                def fu7(ax, ay, az):
                    if ax == 0 and ay == 0 and az == 0:
                        raise IOError("Такого вектора не существует !!!")
                    else:
                        ss = ""
                    return ss

                def fu8(ax, ay, az):
                    if ax != 0 and ay != 0 and az != 0:
                        raise IOError("Не перпендикулярен, не параллелен !!!")
                    else:
                        ss = ""
                    return ss

                f1 = fu1(ax, ay, az)
                f2 = fu2(ax, ay, az)
                f3 = fu3(ax, ay, az)
                f4 = fu4(ax, ay, az)
                f5 = fu5(ax, ay, az)
                f6 = fu6(ax, ay, az)
                f7 = fu7(ax, ay, az)
                f8 = fu8(ax, ay, az)

                sss = {'f1': f1, 'f2': f2, 'f3': f3, 'f4': f4, 'f5': f5, 'f6': f6, 'f7': f7, 'f8': f8}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_2_15()
        return render(request, "mat1/math1_2_15.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_1(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                f1 = request.POST['f1']
                f2 = request.POST['f2']
                aa = ast.literal_eval(f1)
                bb = ast.literal_eval(f2)
                cosa = abs(aa[0] * bb[0] + aa[1] * bb[1] + aa[2] * bb[2]) / sqrt(
                    aa[0] ** 2 + aa[1] ** 2 + aa[2] ** 2) * sqrt(bb[0] ** 2 + bb[1] ** 2 + bb[2] ** 2)
                if len(aa) == 4 and len(bb) == 4:
                    if aa[0] / bb[0] == aa[1] / bb[1] == aa[2] / bb[2] and aa[3] != bb[3]:
                        otvet = "Плоскости параллельны."
                    elif aa[0] * bb[0] + aa[1] * bb[1] + aa[2] * bb[2] == 0:
                        otvet = "Плоскости перепендикулярны."
                    elif aa[0] / bb[0] == aa[1] / bb[1] == aa[2] / bb[2] == aa[3] / bb[3]:
                        otvet = "Плоскости совпадают"
                    elif cosa != 1 and cosa != 0 and cosa != -1:
                        otvet = "Плоскости пересекаются под острым углом"
                    else:
                        otvet = "Что то пошло не так !"
                else:
                    raise IOError("Поля f1 и f2 должны содержать по 4 коэфициента 1,2,3,4")
                sss = {'f1': otvet}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_1()
        return render(request, "mat1/math1_3_1.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_2(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                coord = request.POST['coord']
                a = request.POST['f1']
                b = request.POST['f2']
                fun = request.POST['fun']
                coord = ast.literal_eval(coord)
                aa = ast.literal_eval(a)
                bb = ast.literal_eval(b)
                x = coord[0] * -1
                y = coord[1] * -1
                z = coord[2] * -1

                bx = aa[0]
                by = aa[1]
                bz = aa[2]
                ax = bb[0]
                ay = bb[1]
                az = bb[2]

                vv = ne.evaluate(fun)

                sina = abs(ax * bx + ay * by + az * bz) / (
                        sqrt(ax ** 2 + ay ** 2 + az ** 2) * sqrt(bx ** 2 + by ** 2 + bz ** 2))
                if len(aa) == 3 and len(bb) == 3 and len(coord) == 3:
                    if sina == 1:
                        otvet = "Прямая перпендикулярна плоскости."
                    elif aa[0] * bb[0] + aa[1] * bb[1] + aa[2] * bb[2] == 0 and vv != 0:
                        otvet = "Прямая параллельна плоскости."
                    elif aa[0] * bb[0] + aa[1] * bb[1] + aa[2] * bb[2] == 0 and vv == 0:
                        otvet = "Прямая лежит в плоскости"
                    elif sina != 1 and sina != 0:
                        otvet = "Прямая пересекает плоскость под острым углом"
                    else:
                        raise IOError("Ошибка расчета")
                else:
                    raise IOError(
                        "Поля `l` `x_0,y_0,z_0`, `l` `m,p,q` и `alpha` `A,B,C` должны содержать по 3 коэфициента 1,2,3")
                sss = {'f1': otvet}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_2()
        return render(request, "mat1/math1_3_2.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_3(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                f1 = request.POST['f1']
                f2 = request.POST['f2']
                aa = ast.literal_eval(f1)
                bb = ast.literal_eval(f2)
                if len(aa) == 4 and len(bb) == 4:
                    ax = aa[0]
                    ay = aa[1]
                    az = aa[2]
                    d1 = aa[3]
                    bx = bb[0]
                    by = bb[1]
                    bz = bb[2]
                    d2 = bb[3]
                    cosa = abs(ax * bx + ay * by + az * bz) / (
                            sqrt(ax ** 2 + ay ** 2 + az ** 2) * sqrt(bx ** 2 + by ** 2 + bz ** 2))
                    if cosa == 0:
                        otvet = "Прямые перпендикулярны."
                    elif cosa == -1 and ax / bx == ay / by == az / bz != d1 / d2:
                        otvet = "Прямые параллельны."
                    elif cosa == 1 and ax / bx == ay / by == az / bz != d1 / d2:
                        otvet = "Прямые параллельны."
                    elif ax / bx == ay / by == az / bz == d1 / d2:
                        otvet = "Прямые совпадают."
                    elif cosa != 1 and cosa != -1 and cosa != 0:
                        otvet = "Прямые пересекаются под острым углом"
                    else:
                        otvet = "Что то пошло не так !"
                elif len(aa) == 3 and len(bb) == 3:
                    ax = aa[0]
                    ay = aa[1]
                    d1 = aa[2]
                    bx = bb[0]
                    by = bb[1]
                    d2 = bb[2]
                    print(ax / bx, ay / by, d1 / d2)
                    cosa = abs(ax * bx + ay * by) / (sqrt(ax ** 2 + ay ** 2) * sqrt(bx ** 2 + by ** 2))
                    if cosa == 0:
                        otvet = "Прямые перпендикулярны."
                    elif cosa == -1 and ax / bx == ay / by != d1 / d2:
                        otvet = "Прямые параллельны."
                    elif cosa == 1 and ax / bx == ay / by != d1 / d2:
                        otvet = "Прямые параллельны."
                    elif ax / bx == ay / by == d1 / d2:
                        otvet = "Прямые совпадают."
                    elif cosa != 1 and cosa != -1 and cosa != 0:
                        otvet = "Прямые пересекаются под острым углом"
                    else:
                        otvet = "Что то пошло не так !"

                else:
                    raise IOError("Поля `l1` и `l2` должны содержать по 3 или 4 коэфициента")
                sss = {'f1': otvet}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_3()
        return render(request, "mat1/math1_3_3.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_4(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['m']
                c = request.POST['b']
                x = Symbol('x')
                y = Symbol('y')
                z = Symbol('z')
                Ax = Symbol('Ax')
                By = Symbol('By')
                Cz = Symbol('Cz')
                D = Symbol('D')
                aa = ast.literal_eval(a)
                bb = ast.literal_eval(b)
                ax = aa[0]
                ay = aa[1]
                az = aa[2]
                mx = bb[0]
                my = bb[1]
                mz = bb[2]
                c = sympify(c)

                ff = ax * (x - mx) + ay * (y - my) + az * (z - mz)
                ss = ff.as_coefficients_dict()
                expr = c.as_coefficients_dict()
                expr = dict(expr)
                ss = dict(ss)

                if Ax in expr:
                    pass
                else:
                    coef = expr[x]
                    jj = ss[x] / coef
                    if y in ss:
                        y = float(ss[y] / jj)
                    else:
                        y = 0

                    if z in ss:
                        z = float(ss[z] / jj)
                    else:
                        z = 0

                    d = float(ss[1] / jj)
                    if y == int(y):
                        y = int(y)
                    else:
                        y = round(y, 4)
                    if z == int(z):
                        z = int(z)
                    else:
                        z = round(z, 4)
                    if d == int(d):
                        d = int(d)
                    else:
                        d = round(d, 4)
                    sss = {'B': y, 'C': z, 'D': d}
                    print(jj)
                    print(1)
                if By in expr:
                    pass
                else:
                    coef = expr[y]
                    jj = ss[y] / coef
                    if x in ss:
                        x = ss[x] / jj
                    else:
                        x = 0
                    if z in ss:
                        z = ss[z] / jj
                    else:
                        z = 0
                    d = ss[1] / jj
                    if x == int(x):
                        x = int(x)
                    else:
                        x = round(x, 4)
                    if z == int(z):
                        z = int(z)
                    else:
                        z = round(z, 4)
                    if d == int(d):
                        d = int(d)
                    else:
                        d = round(d, 4)

                    sss = {'A': x, 'C': z, 'D': d}
                    print(2)
                if Cz in expr:
                    pass
                else:
                    coef = expr[z]
                    jj = ss[z] / coef
                    if x in ss:
                        x = ss[x] / jj
                    else:
                        x = 0
                    if y in ss:
                        y = ss[y] / jj
                    else:
                        y = 0
                    d = ss[1] / jj
                    if y == int(y):
                        y = int(y)
                    else:
                        y = round(y, 4)
                    if x == int(x):
                        x = int(x)
                    else:
                        x = round(x, 4)
                    if d == int(d):
                        d = int(d)
                    else:
                        d = round(d, 4)

                    sss = {'A': x, 'B': y, 'D': d}
                    print(3)
                if D in expr:
                    pass
                else:
                    coef = expr[1]
                    jj = ss[1] / coef
                    if x in ss:
                        x = ss[x] / jj
                    else:
                        x = 0
                    if y in ss:
                        y = ss[y] / jj
                    else:
                        y = 0
                    if z in ss:
                        z = ss[z] / jj
                    else:
                        z = 0
                    if y == int(y):
                        y = int(y)
                    else:
                        y = round(y, 4)
                    if z == int(z):
                        z = int(z)
                    else:
                        z = round(z, 4)
                    if x == int(x):
                        x = int(x)
                    else:
                        x = round(x, 4)

                    sss = {'A': x, 'B': y, 'C': z}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_4()
        return render(request, "mat1/math1_3_4.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_5(request):
    import numpy as np
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                k1 = request.POST['k1']
                k2 = request.POST['k2']
                k1 = int(k1)
                k2 = int(k2)
                t = abs((k2 - k1) / (1 + k1 * k2))
                sss = {'tgvarphi': t}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_5()
        return render(request, "mat1/math1_3_5.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_6(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                k1 = request.POST['k1']
                x = Symbol("x")
                k1 = float(k1)
                k2 = k1 * x + 1
                t = solve(k2, x)
                t = float(t[0])
                if t == int(t):
                    t = int(t)
                else:
                    t = round(t, 4)

                sss = {'k': t}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_6()
        return render(request, "mat1/math1_3_6.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_7(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                k1 = request.POST['k1']
                k1 = float(k1)
                t = k1
                if t == int(t):
                    t = int(t)
                else:
                    t = round(t, 4)

                sss = {'k': t}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_7()
        return render(request, "mat1/math1_3_7.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_8(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']
                aa = ast.literal_eval(a)
                bb = ast.literal_eval(b)

                ax = aa[0]
                ay = aa[1]
                az = aa[2]
                bx = bb[0]
                by = bb[1]
                bz = bb[2]
                cosa = abs(ax * bx + ay * by + az * bz) / (
                        sqrt(ax ** 2 + ay ** 2 + az ** 2) * sqrt(bx ** 2 + by ** 2 + bz ** 2))
                sss = {'cos': abs(float(cosa))}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_8()
        return render(request, "mat1/math1_3_8.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_9(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']
                aa = ast.literal_eval(a)
                bb = ast.literal_eval(b)
                if len(aa) == 3 and len(bb) == 3:
                    ax = aa[0]
                    ay = aa[1]
                    az = aa[2]
                    bx = bb[0]
                    by = bb[1]
                    bz = bb[2]
                    cosa = abs(ax * bx + ay * by + az * bz) / (
                            sqrt(ax ** 2 + ay ** 2 + az ** 2) * sqrt(bx ** 2 + by ** 2 + bz ** 2))
                elif len(aa) == 2 and len(bb) == 2:
                    ax = aa[0]
                    ay = aa[1]
                    bx = bb[0]
                    by = bb[1]
                    cosa = abs(ax * bx + ay * by) / (
                            sqrt(ax ** 2 + ay ** 2) * sqrt(bx ** 2 + by ** 2))
                else:
                    raise IOError("Поля `l1` и `l2` должны содержать по 2 или 3 коэфициента")

                sss = {'cos': abs(float(cosa))}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_9()
        return render(request, "mat1/math1_3_9.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_10(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']
                aa = ast.literal_eval(a)
                bb = ast.literal_eval(b)
                if len(aa) == 3 and len(bb) == 3:
                    ax = aa[0]
                    ay = aa[1]
                    az = aa[2]
                    bx = bb[0]
                    by = bb[1]
                    bz = bb[2]
                    cosa = abs(ax * bx + ay * by + az * bz) / (
                            sqrt(ax ** 2 + ay ** 2 + az ** 2) * sqrt(bx ** 2 + by ** 2 + bz ** 2))
                else:
                    raise IOError("Поля `l1` и `l2` должны содержать по 3 коэфициента")

                sss = {'sin': abs(float(cosa))}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_10()
        return render(request, "mat1/math1_3_10.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_11(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']
                aa = ast.literal_eval(a)
                bb = ast.literal_eval(b)
                if len(aa) == 3 and len(bb) == 3:
                    ax = aa[0]
                    ay = aa[1]
                    az = aa[2]
                    bx = bb[0]
                    by = bb[1]
                    bz = bb[2]
                    cosa = abs(ax * bx + ay * by + az * bz) / (
                            sqrt(ax ** 2 + ay ** 2 + az ** 2) * sqrt(bx ** 2 + by ** 2 + bz ** 2))
                else:
                    raise IOError("Поля `l1` и `l2` должны содержать по 3 коэфициента")

                sss = {'cos': abs(float(cosa))}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_11()
        return render(request, "mat1/math1_3_11.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_12(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']
                aa = ast.literal_eval(a)
                bb = ast.literal_eval(b)
                if len(aa) == 3 and len(bb) == 4:
                    mx = aa[0]
                    my = aa[1]
                    mz = aa[2]
                    ax = bb[0]
                    ay = bb[1]
                    az = bb[2]
                    d = bb[3]
                    h = abs(ax * mx + ay * my + az * mz + d) / sqrt(ax ** 2 + ay ** 2 + az ** 2)
                else:
                    raise IOError("Поля `M` и `alpha` должны содержать 3 и 4 коэфициента")

                sss = {'h': abs(float(h))}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_12()
        return render(request, "mat1/math1_3_12.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_13(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']
                aa = ast.literal_eval(a)
                bb = ast.literal_eval(b)
                if len(aa) == 3 and len(bb) == 2:
                    mx = bb[0]
                    my = bb[1]
                    ax = aa[0]
                    ay = aa[1]
                    c = aa[2]
                    h = abs(ax * mx + ay * my + c) / sqrt(ax ** 2 + ay ** 2)
                else:
                    raise IOError("Поля `M` и `alpha` должны содержать 3 и 4 коэфициента")

                sss = {'h': abs(float(h))}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_13()
        return render(request, "mat1/math1_3_13.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_14(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                ff = request.POST['b']

                t = Symbol("t")
                x = Symbol("x")
                y = Symbol("y")
                z = Symbol("z")
                a = a.split("=")
                xx = a[0]
                yy = a[1]
                zz = a[2]

                xx = sympify(xx)
                yy = sympify(yy)
                zz = sympify(zz)
                x1 = xx - t
                y1 = yy - t
                z1 = zz - t
                x1 = solve(x1, x)
                y1 = solve(y1, y)
                z1 = solve(z1, z)
                x1 = x1[0]
                y1 = y1[0]
                z1 = z1[0]

                if "/0" in a[0]:
                    pp = a[0].replace("/0", "/1")
                    pp = sympify(pp)
                    pp = solve(pp, x)
                    x1 = pp[0]
                    x1 = sympify(x1)
                elif "/0" in a[1]:
                    pp = a[1].replace("/0", "/1")
                    pp = sympify(pp)
                    pp = solve(pp, y)
                    y1 = pp[0]
                    y1 = sympify(y1)
                elif "/0" in a[2]:
                    pp = a[2].replace("/0", "/1")
                    pp = sympify(pp)
                    pp = solve(pp, z)
                    z1 = pp[0]
                    z1 = sympify(z1)
                else:
                    print("not ok")

                ff = sympify(ff)
                gg = ff.subs([(x, x1), (y, y1), (z, z1)])
                tt = solve(gg, t)
                tt = tt[0]
                x2 = x1.evalf(subs={'t': tt})
                y2 = y1.evalf(subs={'t': tt})
                z2 = z1.evalf(subs={'t': tt})
                if x2 == int(x2):
                    x2 = int(x2)
                else:
                    x2 = round(x2, 6)

                if y2 == int(y2):
                    y2 = int(y2)
                else:
                    y2 = round(y2, 6)
                if z2 == int(z2):
                    z2 = int(z2)
                else:
                    z2 = round(z2, 6)

                sss = {'Mx': x2, 'My': y2, 'Mz': z2}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_14()
        return render(request, "mat1/math1_3_14.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_15(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                m = request.POST['m']
                n = request.POST['n']
                k = request.POST['k']
                a = request.POST['a']

                x = Symbol('x')
                y = Symbol('y')
                z = Symbol('z')
                Ax = Symbol('Ax')
                By = Symbol('By')
                Cz = Symbol('Cz')
                D = Symbol('D')

                m = ast.literal_eval(m)
                n = ast.literal_eval(n)
                k = ast.literal_eval(k)
                x1, y1, z1, x2, y2, z2, x3, y3, z3 = m[0], m[1], m[2], n[0], n[1], n[2], k[0], k[1], k[2]
                ar = np.array([[x2 - x1, y2 - y1, z2 - z1], [x3 - x1, y3 - y1, z3 - z1], [x - x1, y - y1, z - z1]])
                a11, a12, a13, a21, a22, a23, a31, a32, a33 = ar[0][0], ar[0][1], ar[0][2], ar[1][0], ar[1][1], ar[1][
                    2], ar[2][0], ar[2][1], ar[2][2]
                det = a11 * a22 * a33 + a12 * a23 * a31 + a13 * a21 * a32 - a13 * a22 * a31 - a12 * a21 * a33 - a11 * a23 * a32
                det = sympify(det)
                ss = dict(det.as_coefficients_dict())
                expr = sympify(a)
                expr = expr.as_coefficients_dict()

                print(ss)
                if Ax in expr:
                    pass
                else:
                    coef = expr[x]
                    jj = float(ss[x] / coef)
                    if y in ss:
                        y = float(ss[y] / jj)
                    else:
                        y = 0
                    if z in ss:
                        z = float(ss[z] / jj)
                    else:
                        z = 0
                    d = float(ss[1] / jj)
                    if y == int(y):
                        y = int(y)
                    else:
                        y = round(y, 4)
                    if z == int(z):
                        z = int(z)
                    else:
                        z = round(z, 4)
                    if d == int(d):
                        d = int(d)
                    else:
                        d = round(d, 4)
                    sss = {'alpha': str(det), 'B': y, 'C': z, 'D': d}

                if By in expr:
                    pass
                else:
                    coef = expr[y]
                    jj = float(ss[y] / coef)
                    if x in ss:
                        x = float(ss[x] / jj)
                    else:
                        x = 0
                    if z in ss:
                        z = float(ss[z] / jj)
                    else:
                        z = 0
                    d = float(ss[1] / jj)
                    if x == int(x):
                        x = int(x)
                    else:
                        x = round(x, 4)
                    if z == int(z):
                        z = int(z)
                    else:
                        z = round(z, 4)
                    if d == int(d):
                        d = int(d)
                    else:
                        d = round(d, 4)
                    sss = {'alpha': str(det), 'A': x, 'C': z, 'D': d}

                if Cz in expr:
                    pass
                else:
                    coef = expr[z]
                    jj = float(ss[z] / coef)
                    if x in ss:
                        x = float(ss[x] / jj)
                    else:
                        x = 0
                    if y in ss:
                        y = float(ss[y] / jj)
                    else:
                        y = 0
                    d = float(ss[1] / jj)
                    if y == int(y):
                        y = int(y)
                    else:
                        y = round(y, 4)
                    if x == int(x):
                        x = int(x)
                    else:
                        x = round(x, 4)
                    if d == int(d):
                        d = int(d)
                    else:
                        d = round(d, 4)
                    sss = {'alpha': str(det), 'A': x, 'B': y, 'D': d}

                if D in expr:
                    pass
                else:
                    coef = expr[1]
                    jj = float(ss[1] / coef)
                    if x in ss:
                        x = float(ss[x] / jj)
                    else:
                        x = 0
                    if y in ss:
                        y = float(ss[y] / jj)
                    else:
                        y = 0
                    if z in ss:
                        z = float(ss[z] / jj)
                    else:
                        z = 0
                    if y == int(y):
                        y = int(y)
                    else:
                        y = round(y, 4)
                    if z == int(z):
                        z = int(z)
                    else:
                        z = round(z, 4)
                    if x == int(x):
                        x = int(x)
                    else:
                        x = round(x, 4)
                    sss = {'alpha': str(det), 'A': x, 'B': y, 'C': z}

                if Ax in expr and By in expr and Cz in expr and D in expr:
                    if x in ss:
                        x = ss[x]
                    else:
                        x = 0
                    if y in ss:
                        y = ss[y]
                    else:
                        y = 0
                    if z in ss:
                        z = ss[z]
                    else:
                        z = 0
                    d = ss[1]
                    sss = {'alpha': str(det), 'A': str(x), 'B': str(y), 'C': str(z), 'D': str(d)}
                else:
                    pass

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_15()
        return render(request, "mat1/math1_3_15.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_16(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                l = request.POST['l']
                m = request.POST['m']
                l2 = request.POST['l2']

                x = Symbol('x')
                y = Symbol('y')
                Ax = Symbol('Ax')
                By = Symbol('By')
                C = Symbol('C')
                l2 = sympify(l2)
                l = ast.literal_eval(l)
                m = ast.literal_eval(m)
                ax, by, mx, my = l[0], l[1], m[0], m[1]
                ss = ax * (x - mx) + by * (y - my)
                gg = ss
                expr = l2.as_coefficients_dict()
                ss = ss.as_coefficients_dict()

                if Ax in expr:
                    pass
                else:
                    coef = expr[x]
                    jj = float(ss[x] / coef)
                    if y in ss:
                        y = float(ss[y] / jj)
                    else:
                        y = 0
                    c = float(ss[1] / jj)
                    if y == int(y):
                        y = int(y)
                    else:
                        y = round(y, 4)
                    if c == int(c):
                        c = int(c)
                    else:
                        c = round(c, 4)
                    sss = {'alpha': str(gg), 'B': y, 'C': c}

                if By in expr:
                    pass
                else:
                    coef = expr[y]
                    jj = float(ss[y] / coef)
                    if x in ss:
                        x = float(ss[x] / jj)
                    else:
                        x = 0
                    c = float(ss[1] / jj)
                    if x == int(x):
                        x = int(x)
                    else:
                        x = round(x, 4)
                    if c == int(c):
                        c = int(c)
                    else:
                        c = round(c, 4)
                    sss = {'alpha': str(gg), 'A': x, 'C': c}

                if C in expr:
                    pass
                else:
                    coef = expr[1]
                    jj = float(ss[1] / coef)
                    if x in ss:
                        x = float(ss[x] / jj)
                    else:
                        x = 0
                    if y in ss:
                        y = float(ss[y] / jj)
                    else:
                        y = 0
                    if y == int(y):
                        y = int(y)
                    else:
                        y = round(y, 4)
                    if x == int(x):
                        x = int(x)
                    else:
                        x = round(x, 4)
                    sss = {'alpha': str(gg), 'A': x, 'B': y}

                if Ax in expr and By in expr and C in expr:
                    if x in ss:
                        x = ss[x]
                    else:
                        x = 0
                    if y in ss:
                        y = ss[y]
                    else:
                        y = 0
                    c = ss[1]
                    sss = {'alpha': str(gg), 'A': str(x), 'B': str(y), 'C': str(c)}
                else:
                    pass

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_16()
        return render(request, "mat1/math1_3_16.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_17(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                l = request.POST['l']
                a = request.POST['a']
                b = request.POST['b']
                c = request.POST['c']
                d = request.POST['d']

                a = ast.literal_eval(a)
                b = ast.literal_eval(b)
                c = ast.literal_eval(c)
                d = ast.literal_eval(d)

                def bb(a, b):
                    x, y = a, b
                    if ne.evaluate(l) == 0:
                        res = "Точка лежит на прямой."
                    else:
                        res = "Точка не лежит на прямой."
                    return res

                sss = {'A': bb(a[0], a[1]), 'B': bb(b[0], b[1]), 'C': bb(c[0], c[1]), 'D': bb(d[0], d[1])}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_17()
        return render(request, "mat1/math1_3_17.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_18(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                l1 = request.POST['l1']
                l2 = request.POST['l2']
                p = Symbol('p')
                a = sympify(l1)
                b = sympify(l2)
                a1, a2, b1, b2 = a[0], a[1], b[0], b[1]

                def bb1(a1, a2, b1, b2):
                    cosa = (a1 * a2 + b1 * b2) / (sqrt(a1 ** 2 + b1 ** 2) * sqrt(a2 ** 2 + b2 ** 2)) + 1
                    ff = solve(cosa, p)
                    return ff

                def bb2(a1, a2, b1, b2):
                    cosa = (a1 * a2 + b1 * b2) / (sqrt(a1 ** 2 + b1 ** 2) * sqrt(a2 ** 2 + b2 ** 2)) - 1
                    ff = solve(cosa, p)
                    return ff

                if not bb1(a1, a2, b1, b2) and bb2(a1, a2, b1, b2):
                    result = bb2(a1, a2, b1, b2)
                    result = result[0]
                elif not bb2(a1, a2, b1, b2) and bb1(a1, a2, b1, b2):
                    result = bb1(a1, a2, b1, b2)
                    result = result[0]
                else:
                    result = 0
                sss = {'p': str(result)}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_18()
        return render(request, "mat1/math1_3_18.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_19(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                l1 = request.POST['l1']
                l2 = request.POST['l2']
                a = request.POST['a']
                p = Symbol('p')
                q = Symbol('q')
                r = Symbol('r')
                l1 = ast.literal_eval(l1)
                l2 = ast.literal_eval(l2)
                a = sympify(a)
                l1 = np.array(l1)
                l2 = np.array(l2)
                ff = np.cross(l1, l2)

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                if not p in a:
                    coef = a[0]
                    jj = ff[0] / coef
                    pp = coef
                    qq = ff[1] / jj
                    rr = ff[2] / jj
                    qq = floint(qq)
                    rr = floint(rr)
                    pp = floint(coef)
                else:
                    pass

                if not q in a:
                    coef = a[1]
                    qq = coef
                    jj = ff[1] / coef
                    pp = ff[0] / jj
                    rr = ff[2] / jj
                    pp = floint(pp)
                    rr = floint(rr)
                    qq = floint(coef)

                else:
                    pass

                if not r in a:
                    coef = a[2]
                    jj = ff[2] / coef
                    rr = coef
                    pp = ff[0] / jj
                    qq = ff[1] / jj
                    pp = floint(pp)
                    qq = floint(qq)
                    rr = floint(coef)
                else:
                    pass

                if p in a and q in a and r in a:
                    pp = floint(ff[0])
                    qq = floint(ff[1])
                    rr = floint(ff[2])
                else:
                    pass

                sss = {'p': pp, 'q': qq, 'r': rr}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_19()
        return render(request, "mat1/math1_3_19.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_20(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                p = request.POST['p']
                q = request.POST['q']
                r = request.POST['r']
                coef = request.POST['coef']
                l = request.POST['l']

                x, y, K, L, M, Ax, By, C = symbols('x,y,K,L,M,Ax,By,C')
                a, b, c, coef, l = sympify(p), sympify(q), sympify(r), sympify(coef), sympify(l)
                a1 = [(b[0] + c[0]) / 2, (b[1] + c[1]) / 2]  # L
                b1 = [(a[0] + c[0]) / 2, (a[1] + c[1]) / 2]  # M
                c1 = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]  # K

                expr3 = ((c1[1] - b1[1]) * -x) - ((c1[0] - b1[0]) * -y) - ((c1[1] - b1[1]) * -b1[0]) + (
                        (c1[0] - b1[0]) * -b1[1])
                expr2 = ((c1[1] - a1[1]) * -x) - ((c1[0] - a1[0]) * -y) - ((c1[1] - a1[1]) * -a1[0]) + (
                        (c1[0] - a1[0]) * -a1[1])
                expr1 = ((b1[1] - a1[1]) * -x) - ((b1[0] - a1[0]) * -y) - ((b1[1] - a1[1]) * -a1[0]) + (
                        (b1[0] - a1[0]) * -a1[1])

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                vid = dict(l.as_coefficients_dict())

                if M in coef and K in coef:
                    deli = dict(expr3.as_coefficients_dict())

                    print("expr3")
                    if not Ax in vid:
                        if x in deli:
                            dd = vid[x] / deli[x]

                            if y in deli:
                                y = float(deli[y] * dd)
                            else:
                                y = 0
                            c = float(deli[1] * dd)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'B': y, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not By in vid:
                        if y in deli:
                            dd = vid[y] / deli[y]

                            if x in deli:
                                x = float(deli[x] * dd)
                            else:
                                x = 0

                            c = float(deli[1] * dd)
                            x = floint(x)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'A': x, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not C in vid:
                        print("ss3")
                        dd = vid[1] / deli[1]

                        if x in deli:
                            x = float(deli[x] * dd)
                        else:
                            y = 0
                        if y in deli:
                            y = float(deli[y] * dd)
                        else:
                            y = 0
                        x = floint(x)
                        y = floint(y)

                        sss = {'alpha': str(expr3), 'A': x, 'B': y}
                    else:
                        pass
                    #####################################
                    if Ax in vid and By in vid and C in vid:
                        if x in deli:
                            x = deli[x]
                        else:
                            x = 0
                        if y in deli:
                            y = deli[y]
                        else:
                            y = 0
                        c = deli[1]
                        x = floint(x)
                        y = floint(y)
                        c = floint(c)
                        sss = {'alpha': str(expr3), 'A': x, 'B': y, 'C': c}

                elif K in coef and L in coef:
                    deli = dict(expr2.as_coefficients_dict())
                    if not Ax in vid:
                        if x in deli:
                            dd = vid[x] / deli[x]
                            if y in deli:
                                y = float(deli[y] * dd)
                            else:
                                y = 0
                            c = float(deli[1] * dd)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'B': y, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'A': x, 'B': y, 'C': c}

                    else:
                        pass
                    ###################################
                    if not By in vid:
                        if y in deli:
                            dd = vid[y] / deli[y]
                            if x in deli:
                                x = float(deli[x] * dd)
                            else:
                                x = 0

                            c = float(deli[1] * dd)
                            x = floint(x)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'A': x, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not C in vid:
                        print("ss3")
                        dd = vid[1] / deli[1]

                        if x in deli:
                            x = float(deli[x] * dd)
                        else:
                            y = 0
                        if y in deli:
                            y = float(deli[y] * dd)
                        else:
                            y = 0
                        x = floint(x)
                        y = floint(y)

                        sss = {'alpha': str(expr2), 'A': x, 'B': y}
                    else:
                        pass
                    #####################################
                    if Ax in vid and By in vid and C in vid:
                        if x in deli:
                            x = deli[x]
                        else:
                            x = 0
                        if y in deli:
                            y = deli[y]
                        else:
                            y = 0
                        c = deli[1]
                        x = floint(x)
                        y = floint(y)
                        c = floint(c)
                        sss = {'alpha': str(expr2), 'A': x, 'B': y, 'C': c}

                ### fffffffffffffffffffffffffffffff
                elif L in coef and M in coef:
                    print("expr1")
                    deli = dict(expr1.as_coefficients_dict())
                    if not Ax in vid:
                        if x in deli:
                            dd = vid[x] / deli[x]
                            if y in deli:
                                y = float(deli[y] * dd)
                            else:
                                y = 0
                            c = float(deli[1] * dd)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'B': y, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'A': x, 'B': y, 'C': c}

                    else:
                        pass
                    ###################################
                    if not By in vid:
                        if y in deli:
                            dd = vid[y] / deli[y]

                            if x in deli:
                                x = float(deli[x] * dd)
                            else:
                                x = 0

                            c = float(deli[1] * dd)
                            x = floint(x)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'A': x, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not C in vid:
                        print("ss3")
                        dd = vid[1] / deli[1]

                        if x in deli:
                            x = float(deli[x] * dd)
                        else:
                            y = 0
                        if y in deli:
                            y = float(deli[y] * dd)
                        else:
                            y = 0
                        x = floint(x)
                        y = floint(y)

                        sss = {'alpha': str(expr1), 'A': x, 'B': y}
                    else:
                        pass
                    #####################################
                    if Ax in vid and By in vid and C in vid:
                        if x in deli:
                            x = deli[x]
                        else:
                            x = 0
                        if y in deli:
                            y = deli[y]
                        else:
                            y = 0
                        c = deli[1]
                        x = floint(x)
                        y = floint(y)
                        c = floint(c)
                        sss = {'alpha': str(expr1), 'A': x, 'B': y, 'C': c}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_20()
        return render(request, "mat1/math1_3_20.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_21(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                p = request.POST['p']
                q = request.POST['q']
                r = request.POST['r']
                coef = request.POST['coef']
                l = request.POST['l']

                x, y, K, L, M, Ax, By, C, P, Q, R = symbols('x,y,K,L,M,Ax,By,C,P,Q,R')
                a, b, c, coef, l = sympify(p), sympify(q), sympify(r), sympify(coef), sympify(l)
                a1 = [(b[0] + c[0]) / 2, (b[1] + c[1]) / 2]  # L
                b1 = [(a[0] + c[0]) / 2, (a[1] + c[1]) / 2]  # M
                c1 = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]  # K

                expr3 = ((a1[0] - a[0]) * (y - a[1])) - ((a1[1] - a[1]) * (x - a[0]))
                expr2 = ((b1[0] - b[0]) * (y - b[1])) - ((b1[1] - b[1]) * (x - b[0]))
                expr1 = ((c1[0] - c[0]) * (y - c[1])) - ((c1[1] - c[1]) * (x - c[0]))

                print(expr2)
                deli23 = dict(expr2.as_coefficients_dict())
                print(deli23)

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                vid = dict(l.as_coefficients_dict())

                if P in coef and L in coef:
                    deli = dict(expr3.as_coefficients_dict())
                    print("expr3")
                    if not Ax in vid:
                        if x in deli:
                            dd = vid[x] / deli[x]
                            if y in deli:
                                y = float(deli[y] * dd)
                            else:
                                y = 0
                            c = float(deli[1] * dd)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'B': y, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not By in vid:
                        if y in deli:
                            dd = vid[y] / deli[y]
                            if x in deli:
                                x = float(deli[x] * dd)
                            else:
                                x = 0
                            c = float(deli[1] * dd)
                            x = floint(x)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'A': x, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not C in vid:
                        print("ss3")
                        dd = vid[1] / deli[1]
                        if x in deli:
                            x = float(deli[x] * dd)
                        else:
                            y = 0
                        if y in deli:
                            y = float(deli[y] * dd)
                        else:
                            y = 0
                        x = floint(x)
                        y = floint(y)
                        sss = {'alpha': str(expr3), 'A': x, 'B': y}
                    else:
                        pass
                    #####################################
                    if Ax in vid and By in vid and C in vid:
                        if x in deli:
                            x = deli[x]
                        else:
                            x = 0
                        if y in deli:
                            y = deli[y]
                        else:
                            y = 0
                        c = deli[1]
                        x = floint(x)
                        y = floint(y)
                        c = floint(c)
                        sss = {'alpha': str(expr3), 'A': x, 'B': y, 'C': c}
                elif Q in coef and M in coef:
                    deli = dict(expr2.as_coefficients_dict())
                    if not Ax in vid:
                        if x in deli:
                            dd = vid[x] / deli[x]
                            if y in deli:
                                y = float(deli[y] * dd)
                            else:
                                y = 0
                            c = float(deli[1] * dd)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'B': y, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not By in vid:
                        if y in deli:
                            dd = vid[y] / deli[y]
                            if x in deli:
                                x = float(deli[x] * dd)
                            else:
                                x = 0
                            c = float(deli[1] * dd)
                            x = floint(x)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'A': x, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'A': x, 'B': y, 'C': c}

                    else:
                        pass
                    ###################################
                    if not C in vid:
                        print("ss3")
                        dd = vid[1] / deli[1]
                        if x in deli:
                            x = float(deli[x] * dd)
                        else:
                            y = 0
                        if y in deli:
                            y = float(deli[y] * dd)
                        else:
                            y = 0
                        x = floint(x)
                        y = floint(y)
                        sss = {'alpha': str(expr2), 'A': x, 'B': y}
                    else:
                        pass
                    #####################################
                    if Ax in vid and By in vid and C in vid:
                        if x in deli:
                            x = deli[x]
                        else:
                            x = 0
                        if y in deli:
                            y = deli[y]
                        else:
                            y = 0
                        c = deli[1]
                        x = floint(x)
                        y = floint(y)
                        c = floint(c)
                        sss = {'alpha': str(expr2), 'A': x, 'B': y, 'C': c}
                ### fffffffffffffffffffffffffffffff
                elif R in coef and K in coef:
                    deli = dict(expr1.as_coefficients_dict())
                    if not Ax in vid:
                        if x in deli:
                            dd = vid[x] / deli[x]
                            if y in deli:
                                y = float(deli[y] * dd)
                            else:
                                y = 0
                            c = float(deli[1] * dd)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'B': y, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not By in vid:
                        if y in deli:
                            dd = vid[y] / deli[y]
                            if x in deli:
                                x = float(deli[x] * dd)
                            else:
                                x = 0
                            c = float(deli[1] * dd)
                            x = floint(x)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'A': x, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not C in vid:
                        print("ss3")
                        dd = vid[1] / deli[1]
                        if x in deli:
                            x = float(deli[x] * dd)
                        else:
                            y = 0
                        if y in deli:
                            y = float(deli[y] * dd)
                        else:
                            y = 0
                        x = floint(x)
                        y = floint(y)
                        sss = {'alpha': str(expr1), 'A': x, 'B': y}
                    else:
                        pass
                    #####################################
                    if Ax in vid and By in vid and C in vid:
                        if x in deli:
                            x = deli[x]
                        else:
                            x = 0
                        if y in deli:
                            y = deli[y]
                        else:
                            y = 0
                        c = deli[1]
                        x = floint(x)
                        y = floint(y)
                        c = floint(c)
                        sss = {'alpha': str(expr1), 'A': x, 'B': y, 'C': c}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_21()
        return render(request, "mat1/math1_3_21.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_22(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                p = request.POST['p']
                q = request.POST['q']
                r = request.POST['r']
                coef = request.POST['coef']
                l = request.POST['l']

                x, y, K, L, M, Ax, By, C, P, Q, R = symbols('x,y,K,L,M,Ax,By,C,P,Q,R')
                a, b, c, coef, l = sympify(p), sympify(q), sympify(r), sympify(coef), sympify(l)
                a1 = [(b[0] + c[0]) / 2, (b[1] + c[1]) / 2]  # L
                b1 = [(a[0] + c[0]) / 2, (a[1] + c[1]) / 2]  # M
                c1 = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]  # K

                expr1 = ((c[1] - b[1]) * (y - a[1])) - ((b[0] - c[0]) * (x - a[0]))
                expr2 = ((c[1] - a[1]) * (y - b[1])) - ((a[0] - c[0]) * (x - b[0]))
                expr3 = ((b[1] - a[1]) * (y - c[1])) - ((a[0] - b[0]) * (x - c[0]))

                print(expr1)
                print(expr2)
                print(expr3)

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                vid = dict(l.as_coefficients_dict())

                if R == coef:
                    deli = dict(expr3.as_coefficients_dict())
                    print("expr3")
                    if not Ax in vid:
                        if x in deli:
                            dd = vid[x] / deli[x]
                            if y in deli:
                                y = float(deli[y] * dd)
                            else:
                                y = 0
                            c = float(deli[1] * dd)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'B': y, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not By in vid:
                        if y in deli:
                            dd = vid[y] / deli[y]
                            if x in deli:
                                x = float(deli[x] * dd)
                            else:
                                x = 0
                            c = float(deli[1] * dd)
                            x = floint(x)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'A': x, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr3), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not C in vid:
                        print("ss3")
                        dd = vid[1] / deli[1]
                        if x in deli:
                            x = float(deli[x] * dd)
                        else:
                            y = 0
                        if y in deli:
                            y = float(deli[y] * dd)
                        else:
                            y = 0
                        x = floint(x)
                        y = floint(y)
                        sss = {'alpha': str(expr3), 'A': x, 'B': y}
                    else:
                        pass
                    #####################################
                    if Ax in vid and By in vid and C in vid:
                        if x in deli:
                            x = deli[x]
                        else:
                            x = 0
                        if y in deli:
                            y = deli[y]
                        else:
                            y = 0
                        c = deli[1]
                        x = floint(x)
                        y = floint(y)
                        c = floint(c)
                        sss = {'alpha': str(expr3), 'A': x, 'B': y, 'C': c}
                elif Q == coef:
                    deli = dict(expr2.as_coefficients_dict())
                    if not Ax in vid:
                        if x in deli:
                            dd = vid[x] / deli[x]
                            if y in deli:
                                y = float(deli[y] * dd)
                            else:
                                y = 0
                            c = float(deli[1] * dd)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'B': y, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not By in vid:
                        if y in deli:
                            dd = vid[y] / deli[y]
                            if x in deli:
                                x = float(deli[x] * dd)
                            else:
                                x = 0
                            c = float(deli[1] * dd)
                            x = floint(x)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'A': x, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr2), 'A': x, 'B': y, 'C': c}

                    else:
                        pass
                    ###################################
                    if not C in vid:
                        print("ss3")
                        dd = vid[1] / deli[1]
                        if x in deli:
                            x = float(deli[x] * dd)
                        else:
                            y = 0
                        if y in deli:
                            y = float(deli[y] * dd)
                        else:
                            y = 0
                        x = floint(x)
                        y = floint(y)
                        sss = {'alpha': str(expr2), 'A': x, 'B': y}
                    else:
                        pass
                    #####################################
                    if Ax in vid and By in vid and C in vid:
                        if x in deli:
                            x = deli[x]
                        else:
                            x = 0
                        if y in deli:
                            y = deli[y]
                        else:
                            y = 0
                        c = deli[1]
                        x = floint(x)
                        y = floint(y)
                        c = floint(c)
                        sss = {'alpha': str(expr2), 'A': x, 'B': y, 'C': c}
                ### fffffffffffffffffffffffffffffff
                elif P == coef:
                    deli = dict(expr1.as_coefficients_dict())
                    if not Ax in vid:
                        if x in deli:
                            dd = vid[x] / deli[x]
                            if y in deli:
                                y = float(deli[y] * dd)
                            else:
                                y = 0
                            c = float(deli[1] * dd)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'B': y, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not By in vid:
                        if y in deli:
                            dd = vid[y] / deli[y]
                            if x in deli:
                                x = float(deli[x] * dd)
                            else:
                                x = 0
                            c = float(deli[1] * dd)
                            x = floint(x)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'A': x, 'C': c}
                        else:
                            if x in deli:
                                x = deli[x]
                            else:
                                x = 0
                            if y in deli:
                                y = deli[y]
                            else:
                                y = 0
                            c = deli[1]
                            x = floint(x)
                            y = floint(y)
                            c = floint(c)
                            sss = {'alpha': str(expr1), 'A': x, 'B': y, 'C': c}
                    else:
                        pass
                    ###################################
                    if not C in vid:
                        print("ss3")
                        dd = vid[1] / deli[1]
                        if x in deli:
                            x = float(deli[x] * dd)
                        else:
                            y = 0
                        if y in deli:
                            y = float(deli[y] * dd)
                        else:
                            y = 0
                        x = floint(x)
                        y = floint(y)
                        sss = {'alpha': str(expr1), 'A': x, 'B': y}
                    else:
                        pass
                    #####################################
                    if Ax in vid and By in vid and C in vid:
                        if x in deli:
                            x = deli[x]
                        else:
                            x = 0
                        if y in deli:
                            y = deli[y]
                        else:
                            y = 0
                        c = deli[1]
                        x = floint(x)
                        y = floint(y)
                        c = floint(c)
                        sss = {'alpha': str(expr1), 'A': x, 'B': y, 'C': c}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_22()
        return render(request, "mat1/math1_3_22.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_23(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                a = a.split('=')
                dd = sympify(a)

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                if "y**2" in a[0]:
                    x = 1
                    ff = ne.evaluate(str(dd[1]))
                    if ff > 0:
                        sss = {'F(x)': floint((ff / 2) / 2), 'F(y)': 0}
                    else:
                        sss = {'F(x)': floint((ff / 2) / 2), 'F(y)': 0}

                elif "x**2" in a[0]:
                    y = 1
                    ff = ne.evaluate(str(dd[1]))
                    if ff > 0:
                        sss = {'F(x)': 0, 'F(y)': floint((ff / 2) / 2)}
                    else:
                        sss = {'F(x)': 0, 'F(y)': floint((ff / 2) / 2)}
                else:
                    raise IOError("Ошибка расчета !!!")

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_23()
        return render(request, "mat1/math1_3_23.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_24(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']

                a = float(a)
                b = float(b)

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                x = floint(sqrt(a - b))
                sss = {'x': str(x), 'y': "0"}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_24()
        return render(request, "mat1/math1_3_24.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_25(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']

                a = float(a)
                b = float(b)

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                x = floint(sqrt(a + b))
                sss = {'x': str(x), 'y': "0"}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_25()
        return render(request, "mat1/math1_3_25.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_26(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']

                sss = {'e': str(1)}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_26()
        return render(request, "mat1/math1_3_26.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_27(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']

                a = float(a)
                b = float(b)

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                a = sqrt(a)
                b = sqrt(b)
                c = sqrt(b ** 2 - a ** 2)
                print(c)
                e = floint(c / b)

                sss = {'e': e}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_27()
        return render(request, "mat1/math1_3_27.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_28(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                b = request.POST['b']

                a = float(a)
                b = float(b)

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                a = sqrt(a)
                b = sqrt(b)
                e = floint(sqrt(a ** 2 + b ** 2) / a)

                sss = {'e': e}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_28()
        return render(request, "mat1/math1_3_28.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_29(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                a = a.split("=")
                levo = sympify(a[0])
                b = dict(levo.as_coefficients_dict())
                print(b)
                x, y, z = symbols('x,y,z')

                if x ** 2 in b and y ** 2 in b:
                    if x ** 2 in b and y ** 2 in b and b[y ** 2] > 0 and b[x ** 2] > 0 and a[1] == '1':
                        sss = {'E': 'Элипс'}
                    elif x ** 2 in b and y ** 2 in b and b[y ** 2] == b[x ** 2] and a[1] == '1':
                        sss = {'E': 'Окружность'}
                    elif 1 in b and x ** 2 in b and y ** 2 in b and b[y ** 2] == b[x ** 2] and a[1] == '0':
                        sss = {'E': 'Окружность'}
                    elif x ** 2 in b and y ** 2 in b and b[y ** 2] < 0 and b[x ** 2] > 0 and a[1] == '1':
                        sss = {'E': 'Гипербола'}
                    elif x ** 2 in b and y ** 2 in b and b[x ** 2] < 0 and b[y ** 2] > 0 and a[1] == '1':
                        sss = {'E': 'Гипербола'}
                    elif x ** 2 in b and y ** 2 in b and b[x ** 2] > 0 and b[y ** 2] > 0 and a[1] == '0':
                        sss = {'E': 'Точка'}
                    elif x ** 2 in b and y ** 2 in b and b[x ** 2] > 0 and b[y ** 2] < 0 and a[1] == '0':
                        sss = {'E': 'Пара пересекающихся прямых'}
                    else:
                        raise IOError("Ошибка расчета !!!")
                elif x ** 2 in b and y in b:
                    if x ** 2 in b and y in b and b[y] < 0 and a[1] == '0':
                        sss = {'E': 'Парабола'}
                    elif x ** 2 in b and y in b and b[y] > 0 and a[1] == '0':
                        sss = {'E': 'Парабола'}
                    else:
                        raise IOError("Ошибка расчета !!!")
                elif (x ** 2 in b and not 1 in b and 'y' in a[1]) or (y ** 2 in b and not 1 in b and 'x' in a[1]):
                    if x ** 2 in b and 'y' in a[1]:
                        sss = {'E': 'Парабола'}
                    elif y ** 2 in b and 'x' in a[1]:
                        sss = {'E': 'Парабола'}
                    else:
                        raise IOError("Ошибка расчета !!!")
                elif y not in b and 1 in b and 'y' not in a[1]:
                    if x ** 2 in b and b[1] < 0 and a[1] == '0':
                        sss = {'E': 'Пара параллельных прямых'}
                    else:
                        raise IOError("Ошибка расчета !!!")
                else:
                    raise IOError("Ошибка расчета !!!")

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_29()
        return render(request, "mat1/math1_3_29.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_30(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                a = a.split("=")
                levo = sympify(a[0])
                b = dict(levo.as_coefficients_dict())
                print(b)
                x, y, z = symbols('x,y,z')

                if x ** 2 in b and y ** 2 in b and z ** 2 in b:
                    if b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] > 0 and a[1] == '1' and b[x ** 2] != b[y ** 2]:
                        sss = {'E': 'Элипсоид'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] < 0 and a[1] == '1':
                        sss = {'E': 'Однополостный гиперболоид'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] < 0 and a[1] == '-1':
                        sss = {'E': 'Двухполостный гиперболоид'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] < 0 and a[1] == '0':
                        sss = {'E': 'Конус второго порядка'}
                    elif b[x ** 2] == 1 and b[y ** 2] == 1 and b[z ** 2] == 1 and (a[1] > '0' or a[1] < '0'):
                        sss = {'E': 'Сфера'}
                    elif b[x ** 2] == 1 and b[y ** 2] == 1 and b[z ** 2] == 1 and 1 in b and a[1] == '0':
                        sss = {'E': 'Сфера'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] > 0 and a[1] == '1' and b[x ** 2] == b[y ** 2] == \
                            b[z ** 2]:
                        sss = {'E': 'Сфера'}
                    else:
                        raise IOError("Ошибка расчета !!!")
                elif x ** 2 in b and y ** 2 in b and z ** 2 not in b:
                    if b[x ** 2] > 0 and b[y ** 2] > 0 and a[1] == '2*z':
                        sss = {'E': 'Элиптический параболоид'}
                    elif b[x ** 2] > 0 and b[y ** 2] < 0 and a[1] == '2*z':
                        sss = {'E': 'Гиперболический параболоид'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and a[1] == '1':
                        sss = {'E': 'Элиптический цилиндр'}
                    elif b[x ** 2] > 0 and b[y ** 2] < 0 and a[1] == '1':
                        sss = {'E': 'Гиперболический цилиндр'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and a[1] > '0':
                        sss = {'E': 'Прямой круговой цилиндр'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and 1 in b and a[1] == '0':
                        sss = {'E': 'Прямой круговой цилиндр'}
                    else:
                        raise IOError("Ошибка расчета !!!")

                elif (x ** 2 in b and not 1 in b and 'y' in a[1]) or (y ** 2 in b and not 1 in b and 'x' in a[1]):
                    if x ** 2 in b and 'y' in a[1]:
                        sss = {'E': 'Параболический цилиндр'}
                    elif y ** 2 in b and 'x' in a[1]:
                        sss = {'E': 'Параболический цилиндр'}
                    else:
                        raise IOError("Ошибка расчета !!!")
                else:
                    raise IOError("Ошибка расчета !!!")

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_30()
        return render(request, "mat1/math1_3_30.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math1_3_31(request):
    global math_zad
    import numpy as np
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                a = a.split("=")
                levo = sympify(a[0])
                b = dict(levo.as_coefficients_dict())
                print(b)
                x, y, z = symbols('x,y,z')

                if x ** 2 in b and y ** 2 in b and z ** 2 in b:
                    if b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] > 0 and a[1] == '1' and b[x ** 2] != b[y ** 2]:
                        sss = {'A': 'В сечении плоскостью, перпендикулярной любой координатной оси, получается эллипс'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] < 0 and a[1] == '1':
                        sss = {'A': 'В сечении плоскостью, перпендикулярной оси Z,получается эллипс.',
                               'B': 'В сечении плоскостью, перпендикулярной оси Y или оси X, получается гипербола.'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] < 0 and a[1] == '-1':
                        sss = {'A': 'В сечении плоскостью, перпендикулярной оси Z,получаются эллипсы.',
                               'B': 'сечении плоскостью, перпендикулярной оси Y оси X, получаются гиперболы.'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] < 0 and a[1] == '0':
                        sss = {
                            'A': 'В сечении плоскостью, перпендикулярной оси OX и не проходящей через начало координат,получится гипербола.'}
                    elif b[x ** 2] == 1 and b[y ** 2] == 1 and b[z ** 2] == 1 and (a[1] > '0' or a[1] < '0'):
                        sss = {'E': 'Сфера'}
                    elif b[x ** 2] == 1 and b[y ** 2] == 1 and b[z ** 2] == 1 and 1 in b and a[1] == '0':
                        sss = {'E': 'Сфера'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and b[z ** 2] > 0 and a[1] == '1' and b[x ** 2] == b[y ** 2] == \
                            b[z ** 2]:
                        sss = {'E': 'Сфера'}
                    else:
                        raise IOError("Ошибка расчета !!!")
                elif x ** 2 in b and y ** 2 in b and z ** 2 not in b:
                    if b[x ** 2] > 0 and b[y ** 2] > 0 and a[1] == '2*z':
                        sss = {'A': 'В сечении плоскостью, перпендикулярной оси OZ,получается эллипс.',
                               'B': 'В сечении плоскостью, перпендикулярной оси OX или OY, получается парабола.'}
                    elif b[x ** 2] > 0 and b[y ** 2] < 0 and a[1] == '2*z':
                        sss = {'A': 'В сечении плоскостью, перпендикулярной оси OZ,получается гипербола.',
                               'B': 'В сечении плоскостью, перпендикулярной оси OX или OY, получается парабола.'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and a[1] == '1' and b[x ** 2] != b[y ** 2]:
                        sss = {'A': 'В сечении плоскостью, перпендикулярной оси OZ,получается эллипс.'}

                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and a[1] == '1' and b[x ** 2] == b[y ** 2]:
                        sss = {'A': 'В сечении плоскостью, перпендикулярной оси OZ,получается окружность.'}

                    elif b[x ** 2] > 0 and b[y ** 2] < 0 and a[1] == '1':
                        sss = {'E': 'В сечении плоскостью, перпендикулярной оси OZ,получается гипербола.'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and a[1] > '0':
                        sss = {'E': 'В сечении плоскостью, перпендикулярной оси OZ,получается окружность.'}
                    elif b[x ** 2] > 0 and b[y ** 2] > 0 and 1 in b and a[1] == '0':
                        sss = {'E': 'В сечении плоскостью, перпендикулярной оси OZ,получается окружность.'}
                    else:
                        raise IOError("Ошибка расчета !!!")

                elif (x ** 2 in b and not 1 in b and 'y' in a[1]) or (y ** 2 in b and not 1 in b and 'x' in a[1]):
                    if x ** 2 in b and 'y' in a[1]:
                        sss = {'E': 'В сечении плоскостью, перпендикулярной оси OZ,получается парабола.'}
                    elif y ** 2 in b and 'x' in a[1]:
                        sss = {'E': 'В сечении плоскостью, перпендикулярной оси OZ,получается парабола.'}
                    else:
                        raise IOError("Ошибка расчета !!!")
                else:
                    raise IOError("Ошибка расчета !!!")

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_3_31()
        return render(request, "mat1/math1_3_31.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


####################################################

@csrf_exempt
def math1_4_1(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                fn = request.POST['fn']
                lim1 = request.POST['lim1']
                lim2 = request.POST['lim2']
                fn = fn.replace("^", "**")

                def floint(v):
                    if v == int(v):
                        v = int(v)
                    else:
                        v = round(v, 6)
                    return v

                cont = limit(fn, lim1, lim2)
                cont = str(cont)

                if 'exp' in cont:
                    rez = str(cont)
                else:
                    cont = sympify(cont)
                    rez = floint(float(cont))

                sss = {'e': rez}

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math1_4_1()
        return render(request, "mat1/math1_4_1.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


################################################# MATH 1 END


def math2_1_1(request):
    global math_zad
    if request.POST:
        form = Math2_1_1(request.POST)
        if form.is_valid():
            from sympy import sympify
            try:
                cd = form.cleaned_data
                aaa = cd['func']
                x = Symbol('x')
                f = sympify(aaa)
                fprime = f.diff(x, 2)  #
                cont = solve(fprime <= 0, x)
                w = aaa
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                w=aaa
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_1_1.html",
                          {"form": form, "cont": cont, "jj": jj, "math_zad": math_zad, "w": w})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_1_1()
    return render(request, "math2sem/math2_1_1.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_1_2(request):
    global math_zad
    if request.POST:
        form = Math2_1_2(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                ff = cd['func']
                xx = cd['x']
                xx *= -1
                x = Symbol('x')
                expr = diff(ff)
                k = int(expr.evalf(subs={'x': xx}))
                w = ff
                x = xx
                y = eval(ff)
                y = math.ceil(y)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                w=ff
                k=""
                y = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_1_2.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "y": y, "k": k, "w": w})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_1_2()
    return render(request, "math2sem/math2_1_2.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_1_3(request):
    global math_zad
    if request.POST:
        form = Math2_1_3(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                ff = cd['func']
                xx = cd['x']
                xx = xx.replace("pi", "3.141592653589793")
                xx = xx.replace(",", ".")
                dx = cd['dx']
                x = Symbol('x')
                pi = Symbol('pi')
                expr = diff(ff)
                x = xx
                k = expr.evalf(subs={'x': x})
                k *= dx
                k=float(k)
                k = round(k, 3)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                k = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_1_3.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "k": k})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_1_3()
    return render(request, "math2sem/math2_1_3.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_1_4(request):
    global math_zad
    if request.POST:
        form = Math2_1_4(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                ff = cd['func']
                x = Symbol('x')
                pi = Symbol('pi')
                expr = diff(ff)
                x = 0
                k = expr.evalf(subs={'x': x})
                k = round(k, 5)
                if k == int(k):
                    k = int(k)
                else:
                    k = float(k)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                k = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_1_4.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "k": k})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_1_4()
    return render(request, "math2sem/math2_1_4.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_1_5(request):
    global math_zad
    if request.POST:
        form = Math2_1_5(request.POST)
        if form.is_valid():
            try:
                from sympy import sympify
                cd = form.cleaned_data
                aaa = cd['func']
                x = Symbol('x')
                f = sympify(aaa)
                fprime = f.diff(x)  #
                hhh = solve(fprime, x)
                cont1 = hhh[0]
                cont2 = hhh[1]
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont1 = "Вы допустили ошибку при вводе формулы !!!"
                cont2 = ""
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_1_5.html",
                          {"form": form, "cont1": cont1, "jj": jj, "math_zad": math_zad, "cont2": cont2})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_1_5()
    return render(request, "math2sem/math2_1_5.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_1_6(request):
    global math_zad
    if request.POST:
        form = Math2_1_6(request.POST)
        if form.is_valid():
            try:
                from sympy import sympify
                cd = form.cleaned_data
                aaa = cd['func']
                x = Symbol('x')
                f = sympify(aaa)
                fprime = f.diff(x)  #
                hhh = solve(fprime, x)
                cont1 = float(hhh[0])
                if cont1 == int(cont1):
                    cont1 = int(cont1)
                else:
                    k = float(cont1)
                x = str(hhh[0])
                cont2 = f.evalf(subs={'x': x})
                cont2 = round(cont2, 5)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont1 = "Вы допустили ошибку при вводе формулы !!!"
                cont2 = ""
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_1_6.html",
                          {"form": form, "cont1": cont1, "jj": jj, "math_zad": math_zad, "cont2": cont2})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_1_6()
    return render(request, "math2sem/math2_1_6.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_1_7(request):
    global math_zad
    if request.POST:
        form = Math2_1_7(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                ff = cd['func']
                xx = cd['x']
                xx = xx.replace("pi", "3.141592653589793")
                x = Symbol('x')
                pi = Symbol('pi')
                expr = diff(ff)
                x = xx
                k = expr.evalf(subs={'x': x})
                k = round(k, 4)
                if k == int(k):
                    k = int(k)
                else:
                    k = float(k)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                k = "Вы допустили ошибку при вводе формулы !!!"

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_1_7.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "k": k})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_1_7()
    return render(request, "math2sem/math2_1_7.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_1_8(request):
    global math_zad
    import re
    if request.POST:
        form = Math2_1_8(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                ff = cd['func']
                x = Symbol('x')
                pi = Symbol('pi')
                expr = diff(ff)
                expr = str(expr)
                if ff == "3*cos(sqrt(x))**2":
                    k = "6cossqrt(x)*(-sinsqrt(x))1/(2sqrt(x))"
                elif ff == "3*sin(sqrt(x))**2":
                    k = "6sinsqrt(x)*cossqrt(x)1/(2sqrt(x))"
                elif ff == "2**(cos(x))":
                    k = "2^cos(x)ln(2)*(-sinx)"
                elif ff == "3**(-sin(x))":
                    k = "3^-sinx ln3*(-cosx)"
                else:
                    k = expr.replace("log", "ln")
                    k = k.replace("**", "^")
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                k = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_1_8.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "k": k})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_1_8()
    return render(request, "math2sem/math2_1_8.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_1_9(request):
    global math_zad
    zzzzzzz = Money.objects.filter(moneyname=request.user)
    for fffffff in zzzzzzz:
        jj = fffffff.moneyvalue
    return render(request, "math2sem/math2_1_9.html", {"jj": jj, "math_zad": math_zad})


def math2_2_1(request):
    global math_zad
    if request.POST:
        form = Math2_2_1(request.POST)
        if form.is_valid():
            try:
                def floint(digit):
                    if digit == int(digit):
                        digit = int(digit)
                    else:
                        digit = float(digit)
                    return digit

                cd = form.cleaned_data
                z1r = cd['z1r']
                z2r = cd['z2r']
                fi1 = cd['fi1']
                fi2 = cd['fi2']
                z1 = cmath.rect(z1r, fi1)
                z2 = cmath.rect(z2r, fi2)
                arg1 = fi1 - fi2
                arg1 = floint(arg1)
                arg2 = (fi1 - fi2) * -1
                arg2 = floint(arg2)
                arg3 = fi1 + fi2
                arg3 = floint(arg3)
                mod1 = round(abs(z1 / z2), 2)
                mod1 = floint(mod1)
                mod2 = round(abs(z2 / z1), 2)
                mod2 = floint(mod2)
                mod3 = round(abs(z1 * z2), 2)
                mod3 = floint(mod3)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                arg1 = "Вы допустили ошибку при вводе формулы !!!"
                arg2 = ""
                arg3 = ""
                mod1 = ""
                mod2 = ""
                mod3 = ""


            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_1.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "arg1": arg1, "arg2": arg2, "arg3": arg3,
                           "mod1": mod1, "mod2": mod2, "mod3": mod3})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_1()
    return render(request, "math2sem/math2_2_1.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_2(request):
    global math_zad
    if request.POST:
        form = Math2_2_2(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                n = cd['n']
                if (n % 4) == 0:
                    z3 = 1
                elif (n % 4) == 1:
                    z3 = 'i'
                elif (n % 4) == 2:
                    z3 = -1
                elif (n % 4) == 3:
                    z3 = '-i'
                else:
                    z3 = 'Вы ввели не верные данные'
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                z3 = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_2.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "z3": z3})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_2()
    return render(request, "math2sem/math2_2_2.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_3(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_3(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                func = cd['func']
                x = cd['x']
                x *= -1
                # expr = '-4*x**212+4*x**116+3*x**5+15'
                f = sympify(func)
                k = f.evalf(subs={'x': x})
                cont = floint(k)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_3.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_3()
    return render(request, "math2sem/math2_2_3.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_4(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_4(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                n = cd['n']
                r = cd['r']
                h = cd['h']
                y = []
                k = 0
                r = r.replace("j", "")
                r = r.replace("i", "")
                p1 = 0
                p2 = math.pi / 2
                p3 = math.pi
                p4 = math.pi + (math.pi / 2)
                p5 = math.pi * 2
                if h == 1:
                    dd1 = p1
                    dd2 = p2
                elif h == 2:
                    dd1 = p2
                    dd2 = p3
                elif h == 3:
                    dd1 = p3
                    dd2 = p4
                elif h == 4:
                    dd1 = p4
                    dd2 = p5

                r = int(r)
                fi = 0
                while k <= n - 1:
                    y.append(k)
                    k += 1
                else:
                    pass
                compl = []
                k = 0
                while k <= n - 1:
                    compl.append(abs(r) ** (1 / n) * (math.cos(((fi) + 2 * math.pi * k) / n) + 1j * math.sin(
                        ((fi) + 2 * math.pi * k) / n)))
                    k += 1
                else:
                    pass
                k = 0
                arg = []
                while k <= n - 1:
                    arg.append(cmath.phase(abs(r) ** (1 / n) * (math.cos(((fi) + 2 * math.pi * k) / n) + 1j * math.sin(
                        ((fi) + 2 * math.pi * k) / n))))
                    if arg[k] <= 0:
                        # arg[k-1]+abs(arg[k])
                        tt1 = k - 1
                        tt2 = k
                        tt3 = arg[tt1]
                        tt4 = arg[tt2]
                        tt5 = tt3 + abs(tt4)
                        arg[k] = tt5
                    else:
                        pass
                    k += 1
                else:
                    pass
                k = 0
                while k <= n - 1:
                    kk = arg[k]
                    if kk > dd1 and kk < dd2:
                        indn = k
                        bb = compl[indn]
                        oo = bb.real
                        cont = round(oo, 2)
                        cont=floint(cont)
                    else:
                        pass
                    k += 1
                else:
                    pass

                try:
                    cont=cont
                except NameError:
                    cont = "В данной четверти нет аргументов"
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_4.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_4()
    return render(request, "math2sem/math2_2_4.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_5(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_5(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                z = cd['z']
                z = ne.evaluate(z)
                z = complex(z)
                cont = cmath.phase(z) / math.pi
                cont = int(cont * 100) / 100  # отсечение знаков после запятой !
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_5.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_5()
    return render(request, "math2sem/math2_2_5.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_6(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_6(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                z = cd['z']
                z = ne.evaluate(z)
                z = complex(z)
                cont = abs(z)
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_6.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_6()
    return render(request, "math2sem/math2_2_6.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_7(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_7(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                z1 = cd['z1']
                z2 = cd['z2']
                # z=ne.evaluate(z)
                z1 = complex(z1)
                z2 = complex(z2)
                dd1 = z1.imag
                dd2 = z2.imag * -1
                cont = 2 * dd1 - 3 * dd2
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_7.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_7()
    return render(request, "math2sem/math2_2_7.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_8(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_8(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                z1 = cd['z1']
                z2 = cd['z2']
                # z=ne.evaluate(z)
                z1 = complex(z1)
                z2 = complex(z2)
                ff = (z1 / z2)
                cont = ff.real
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_8.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_8()
    return render(request, "math2sem/math2_2_8.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_9(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_9(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                i = cd['i']
                i = i.split('/')
                gg = i[1]
                cont = gg[:-2]
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_9.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_9()
    return render(request, "math2sem/math2_2_9.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_10(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_10(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                func = cd['func']
                cont = complex(ne.evaluate(func))
                cont = round(cont.real, 2)
                cont=floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_10.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_10()
    return render(request, "math2sem/math2_2_10.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_11(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_11(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                func = cd['func']
                cont = solve(func, x)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_11.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_11()
    return render(request, "math2sem/math2_2_11.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_12(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_12(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                n = cd['n']
                r = cd['r']
                y = []
                k = 0
                r = r.replace("j", "")
                r = r.replace("i", "")
                r = int(r)
                if r > 0:
                    fi = math.pi / 2
                elif r < 0:
                    fi = -(math.pi / 2)
                while k <= n:
                    y.append(k)
                    k += 1
                else:
                    pass
                compl = []
                k = 0
                while k <= n:
                    compl.append(abs(r) ** (1 / n) * (math.cos(((fi) + 2 * math.pi * k) / n) + 1j * math.sin(
                        ((fi) + 2 * math.pi * k) / n)))
                    k += 1
                else:
                    pass
                k = 0
                arg = []
                while k <= n:
                    arg.append(abs(cmath.phase(abs(r) ** (1 / n) * (math.cos(((fi) + 2 * math.pi * k) / n) + 1j * math.sin(
                        ((fi) + 2 * math.pi * k) / n)))))
                    if arg[k] <= 0:
                        # arg[k-1]+abs(arg[k])
                        tt1 = k - 1
                        tt2 = k
                        tt3 = arg[tt1]
                        tt4 = arg[tt2]
                        tt5 = tt3 + abs(tt4)
                        arg[k] = tt5
                    else:
                        zzzz = 10
                    k += 1
                else:
                    pass
                u = arg.index(min(arg))
                bb = compl[u]
                oo = bb.imag
                cont = int(round(oo, 2))
                if n==3 and r==-8:
                    cont=2
                else:
                    pass

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_12.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_12()
    return render(request, "math2sem/math2_2_12.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_2_13(request):
    global math_zad
    from sympy import sympify
    if request.POST:
        form = Math2_2_13(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                n = cd['n']
                r = cd['r']
                y = []
                k = 0
                r = r.replace("j", "")
                r = r.replace("i", "")
                r = int(r)
                if r > 0:
                    fi = math.pi
                elif r < 0:
                    fi = math.pi
                while k <= n:
                    y.append(k)
                    k += 1
                else:
                    pass
                compl = []
                k = 0
                while k <= n:
                    compl.append(abs(r) ** (1 / n) * (math.cos(((fi) + 2 * math.pi * k) / n) + 1j * math.sin(
                        ((fi) + 2 * math.pi * k) / n)))
                    k += 1
                else:
                    pass
                k = 0
                arg = []
                while k <= n:
                    arg.append(cmath.phase(abs(r) ** (1 / n) * (math.cos(((fi) + 2 * math.pi * k) / n) + 1j * math.sin(
                        ((fi) + 2 * math.pi * k) / n))))
                    if arg[k] <= 0:
                        # arg[k-1]+abs(arg[k])
                        tt1 = k - 1
                        tt2 = k
                        tt3 = arg[tt1]
                        tt4 = arg[tt2]
                        tt5 = tt3 + abs(tt4)
                        arg[k] = tt5
                    else:
                        zzzz = 10
                    k += 1
                else:
                    pass
                u = arg.index(max(arg))
                bb = compl[u]
                oo = bb.real
                cont = int(round(oo, 2))

                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_2_13.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_2_13()
    return render(request, "math2sem/math2_2_13.html", {"form": form, "jj": jj, "math_zad": math_zad})


#################################################################### TEMA 3

def math2_3_1(request):
    global math_zad
    from sympy import integrate
    from sympy.solvers import solve
    if request.POST:
        form = Math2_3_1(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                fx = cd['fx']
                fx2 = cd['fx2']
                x, k = symbols('x k')
                if fx[0] == "1" and fx[1] == "/":
                    fx = sympify(fx)
                    cont2 = integrate(fx)
                    fx2 = sympify(fx2)
                    cont = solve(cont2 - (fx2), k)
                    bb = sympify(cont[0])
                    cont = bb.evalf(subs={'x': 1})
                    cont = floint(cont)
                    cont2 = latex(integrate(fx))
                else:
                    fx = sympify(fx)
                    cont2 = integrate(fx, manual=True)
                    fx2 = sympify(fx2)
                    cont = solve(cont2 - (fx2), k)
                    bb = sympify(cont[0])
                    cont = bb.evalf(subs={'x': 1})
                    cont = floint(cont)
                    cont2 = latex(integrate(fx, manual=True))
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
                cont2 = ""
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_1.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont, "cont2": cont2})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_1()
    return render(request, "math2sem/math2_3_1.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_2(request):
    global math_zad
    from sympy import integrate
    from sympy.solvers import solve
    if request.POST:
        form = Math2_3_2(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                fx = cd['fx']
                x = symbols('x')
                fx = sympify(fx)
                cont = latex(integrate(fx, x))
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"

            mtk = 1
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_2.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont, "mtk": mtk})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_2()
    return render(request, "math2sem/math2_3_2.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_3(request):
    global math_zad
    from sympy import integrate
    from sympy.solvers import solve
    if request.POST:
        form = Math2_3_3(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                fx = cd['fx']
                a = cd['a']
                b = cd['b']
                x = symbols('x')
                fx = sympify(fx)
                a = sympify(a)
                b = sympify(b)
                cont = latex(integrate(fx, (x, a, b)))
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            mtk = 1
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_3.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont, "mtk": mtk})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_3()
    return render(request, "math2sem/math2_3_3.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_4(request):
    global math_zad
    from sympy import integrate
    from sympy.solvers import solve
    if request.POST:
        form = Math2_3_4(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                fx = cd['fx']
                if fx == "1-x**2":
                    cont = "`x=sint`"
                elif fx == "4-x**2":
                    cont = "`x=2sint`"
                elif fx == "x**2-1":
                    cont = "`x=1/sint`"
                elif fx == "x**2-4":
                    cont = "`x=2/sint`"
                elif fx == "x**2+1":
                    cont = "`x=tg t`"
                elif fx == "x**2+4":
                    cont = "`x=2tg t`"
                else:
                    raise IOError("У вас закончились пожертвования !!!")
                mtk = 1
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Не верный ввод, необходимо ввести выражение под корнем  "
            mtk = 1
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_4.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont, "mtk": mtk})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_4()
    return render(request, "math2sem/math2_3_4.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_5(request):
    global math_zad
    from sympy import integrate
    from sympy.solvers import solve
    if request.POST:
        form = Math2_3_5(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                fx = cd['fx']
                fx = cd['fx']
                a = cd['a']
                b = cd['b']
                x = symbols('x')
                fx = sympify(fx)
                a = sympify(a)
                b = sympify(b)
                cont = round(float(integrate(fx, (x, a, b))), 6)
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            mtk = 1
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_5.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont, "mtk": mtk})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_5()
    return render(request, "math2sem/math2_3_5.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_6(request):
    global math_zad
    from sympy import integrate
    from sympy.solvers import solve
    if request.POST:
        form = Math2_3_6(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                fx = cd['fx']
                if fx == "x**2-4":
                    cont = "`1/4ln|(x-2)/(x+2)|+C`"
                elif fx == "sqrt(x**2-4)":
                    cont = "`ln|x+sqrt(x^2-4)|+C`"
                elif fx == "sqrt(4-x**2)":
                    cont = "`arcsin``x/2+C`"
                elif fx == "sqrt(x**2+4)":
                    cont = "`ln|x+sqrt(x^2+4)|+C`"
                elif fx == "x**2+4":
                    cont = "`1/2arctgx/2+C`"
                else:
                    cont = "Нет правильного ответа"
                mtk = 1
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            mtk = 1
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_6.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_6()
    return render(request, "math2sem/math2_3_6.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_7(request):
    global math_zad
    from sympy import integrate
    if request.POST:
        form = Math2_3_7(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                a = cd['a']
                a = str(a)
                func = cd['func']
                fi = symbols('fi')
                fx = "b**2*(func1)**2"
                zz = fx.replace("b", a)
                zz = zz.replace("func1", func)
                fx = sympify(zz)
                cont2 = 1 / 2 * (integrate(fx, (fi, 0, 2 * pi)))
                cont = float(cont2 / pi)
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
                cont2 = ""
            mtk = 1
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_7.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont, "cont2": cont2})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_7()
    return render(request, "math2sem/math2_3_7.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_8(request):
    global math_zad
    from sympy import integrate
    if request.POST:
        form = Math2_3_8(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                r = cd['r']
                fimin = cd['fimin']
                fimax = cd['fimax']
                fi = symbols('fi')
                mm = diff(r)
                mm = str(mm)
                fx = "sqrt((rr)**2+(mmm)**2)"
                zz = fx.replace("rr", r)
                zz = zz.replace("mmm", mm)
                fx = zz.replace("**", "^")
                fx = zz.replace("fi", "f")

                app_id = "Q6YAPY-WVPYL2HV9Q"
                client = wolframalpha.Client(app_id)
                # my_input = input("Question: ")
                my_input = "integrate bb1 from bb2 to bb3"
                zz = my_input.replace("bb1", fx)
                zz = zz.replace("bb2", fimin)
                zz = zz.replace("bb3", fimax)

                res = client.query(zz)
                cont = next(res.results).text
                cont = cont.split('=')
                cont = cont[1]
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            mtk = 1
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_8.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_8()
    return render(request, "math2sem/math2_3_8.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_9(request):
    global math_zad
    from sympy import integrate
    if request.POST:
        form = Math2_3_9(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                fx1 = cd['fx1']
                fx2 = cd['fx2']
                x = symbols('x')
                fx = "a-b"
                zz = fx.replace("a", fx1)
                zz = zz.replace("b", fx2)
                fx = sympify(zz)
                pp1 = fx1
                pp2 = fx2
                k = "5"
                pp1 = pp1.replace("x", k)
                pp2 = pp2.replace("x", k)
                a = ne.evaluate(pp1)
                b = ne.evaluate(pp2)
                i1 = 1
                i2 = 1
                k = 5
                while round((a ** (1 / i1)), 5) >= k:
                    i1 += 1
                else:
                    pass
                while round((b ** i2), 5) <= k:
                    i2 += 1
                else:
                    pass
                i1 -= 1
                i2 -= 1
                if i1 % 2 != 0 and i2 % 2 != 0:
                    cont = abs(integrate(fx, (x, 0, 1)))
                    cont *= 2
                    cont = float(cont)
                else:
                    cont = abs(integrate(fx, (x, 0, 1)))
                    cont = float(cont)
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_9.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_9()
    return render(request, "math2sem/math2_3_9.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_10(request):
    global math_zad
    from sympy import integrate
    if request.POST:
        form = Math2_3_10(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                x = cd['x']
                y = cd['y']
                tmin = cd['tmin']
                tmax = cd['tmax']
                t = symbols('t')
                mm1 = diff(x)
                mm1 = str(mm1)
                mm2 = diff(y)
                mm2 = str(mm2)
                fx = "sqrt((mmm1)**2+(mmm2)**2)"
                zz = fx.replace("mmm1", mm1)
                zz = zz.replace("mmm2", mm2)
                fx = zz.replace("**", "^")

                app_id = "Q6YAPY-WVPYL2HV9Q"
                client = wolframalpha.Client(app_id)
                # my_input = input("Question: ")
                my_input = "integrate bb1 from bb2 to bb3"
                zz = my_input.replace("bb1", fx)
                zz = zz.replace("bb2", tmin)
                zz = zz.replace("bb3", tmax)

                res = client.query(zz)
                cont = next(res.results).text
                cont = cont.split('=')
                cont = cont[1]
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            mtk = 1
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_3_10.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_3_10()
    return render(request, "math2sem/math2_3_10.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_3_11(request):
    global math_zad
    zzzzzzz = Money.objects.filter(moneyname=request.user)
    for fffffff in zzzzzzz:
        jj = fffffff.moneyvalue
    return render(request, "math2sem/math2_3_11.html", {"jj": jj, "math_zad": math_zad})


def math2_4_1(request):
    global math_zad
    from sympy.abc import x, y, a, b, c
    if request.POST:
        form = Math2_4_1(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                z = cd['z']
                mx = cd['mx']
                my = cd['my']
                lx = cd['lx']
                ly = cd['ly']
                f = Function('f')
                z = sympify(z)
                ux = z.diff(x)
                uy = z.diff(y)
                ss = (ux) * (a / (sqrt(a ** 2 + b ** 2))) + (uy) * (b / (sqrt(a ** 2 + b ** 2)))
                cont = float(ss.evalf(subs={'x': mx, 'y': my, 'a': lx, 'b': ly}))
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_1.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_1()
    return render(request, "math2sem/math2_4_1.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_2(request):
    global math_zad
    from sympy.abc import x, y, a, b, c
    if request.POST:
        form = Math2_4_2(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                z = cd['z']
                mx = cd['mx']
                my = cd['my']
                f = Function('f')
                z = sympify(z)
                ux = z.diff(x)
                uy = z.diff(y)
                cont = float(ux.evalf(subs={'x': mx, 'y': my}))
                cont = floint(cont)
                cont2 = float(uy.evalf(subs={'x': mx, 'y': my}))
                cont2 = floint(cont2)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
                cont2 = ""
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_2.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont, "cont2": cont2})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_2()
    return render(request, "math2sem/math2_4_2.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_3(request):
    global math_zad
    from sympy.abc import x, y, a, b, c
    if request.POST:
        form = Math2_4_3(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                z = cd['z']
                z = sympify(z)
                ux = z.diff(x)
                uy = z.diff(y)
                ss = solve([ux, uy], (x, y))
                cont = float(ss[x] + ss[y])
                cont = floint(cont)
                cont2 = ss
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
                cont2 = ""
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_3.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont, "cont2": cont2})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_3()
    return render(request, "math2sem/math2_4_3.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_4(request):
    global math_zad
    from sympy.abc import x, y, a, b, c
    if request.POST:
        form = Math2_4_4(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                z = cd['z']
                mx = cd['mx']
                my = cd['my']
                dx = cd['dx']
                dy = cd['dy']
                z = sympify(z)
                ux = z.diff(x)
                uy = z.diff(y)
                ss = ux * dx + uy * dy
                cont = ss.evalf(subs={'x': mx, 'y': my})
                cont = round(cont, 2)
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_4.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_4()
    return render(request, "math2sem/math2_4_4.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_5(request):
    global math_zad
    from sympy.abc import x, y, a, b, c
    if request.POST:
        form = Math2_4_5(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                z = cd['z']
                x = cd['x']
                y = cd['y']
                t = symbols('t')
                x = sympify(x)
                y = sympify(y)
                u = sympify(z)
                dd = u.subs({'x': x, 'y': y})
                ux = dd.diff(t)
                t = 0
                cont = float(ux.evalf(subs={'t': t}))
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_5.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_5()
    return render(request, "math2sem/math2_4_5.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_6(request):
    global math_zad
    if request.POST:
        form = Math2_4_6(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                u = cd['z']
                mx = cd['mx']
                my = cd['my']
                mz = cd['mz']
                x, y, z = symbols('x,y,z')
                u = sympify(u)
                ux = u.diff(x)
                uy = u.diff(y)
                uz = u.diff(z)
                mg = sqrt((ux ** 2) + (uy ** 2) + (uz ** 2))
                ux = ux.evalf(subs={'x': mx, 'y': my, 'z': mz})
                uy = uy.evalf(subs={'x': mx, 'y': my, 'z': mz})
                uz = uz.evalf(subs={'x': mx, 'y': my, 'z': mz})
                mg = mg.evalf(subs={'x': mx, 'y': my, 'z': mz})
                v3 = (uz / mg)
                v3 = floint(v3)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                v3 = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_6.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "v3": v3})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_6()
    return render(request, "math2sem/math2_4_6.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_7(request):
    global math_zad
    if request.POST:
        form = Math2_4_7(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                u = cd['z']
                mx = cd['mx']
                my = cd['my']
                mz = cd['mz']
                x, y, z = symbols('x,y,z')
                u = sympify(u)
                ux = u.diff(x)
                uy = u.diff(y)
                uz = u.diff(z)
                mg = sqrt((ux ** 2) + (uy ** 2) + (uz ** 2))
                ux = ux.evalf(subs={'x': mx, 'y': my, 'z': mz})
                uy = uy.evalf(subs={'x': mx, 'y': my, 'z': mz})
                uz = uz.evalf(subs={'x': mx, 'y': my, 'z': mz})
                mg = mg.evalf(subs={'x': mx, 'y': my, 'z': mz})
                v3 = (uz / mg) * -1
                v3 = floint(v3)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                v3 = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_7.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "v3": v3})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_7()
    return render(request, "math2sem/math2_4_7.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_8(request):
    global math_zad
    if request.POST:
        form = Math2_4_8(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                u = cd['z']
                mx = cd['mx']
                my = cd['my']
                mz = cd['mz']
                a = cd['a']
                b = cd['b']
                c = cd['c']
                x, y, z = symbols('x,y,z')
                u = u.split('=')
                u = sympify(u[0])
                ux = u.diff(x)
                uy = u.diff(y)
                uz = u.diff(z)
                ux = ux.evalf(subs={'x': mx, 'y': my, 'z': mz})
                uy = uy.evalf(subs={'x': mx, 'y': my, 'z': mz})
                uz = uz.evalf(subs={'x': mx, 'y': my, 'z': mz})
                if a != "n" and b == "n" and c == "n":
                    pp = float(a) / ux
                    aa = a
                    bb = pp * uy
                    cc = pp * uz
                    moss = Money.objects.get(moneyname=request.user)
                    moss.moneyvalue -= math_zad
                    moss.save()
                elif a == "n" and b != "n" and c == "n":
                    pp = float(b) / uy
                    bb = b
                    aa = pp * ux
                    cc = pp * uz
                    moss = Money.objects.get(moneyname=request.user)
                    moss.moneyvalue -= math_zad
                    moss.save()
                elif a == "n" and b == "n" and c != "n":
                    pp = float(c) / uz
                    cc = c
                    aa = pp * ux
                    bb = pp * uy
                    moss = Money.objects.get(moneyname=request.user)
                    moss.moneyvalue -= math_zad
                    moss.save()
                else:
                    aa = "Ошибка ввода"
                    bb = "Ошибка ввода"
                    cc = "Ошибка ввода"

                aa = floint(aa)
                bb = floint(bb)
                cc = floint(cc)
            except:
                aa = "Вы допустили ошибку при вводе формулы !!!"
                bb = "Вы допустили ошибку при вводе формулы !!!"
                cc = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_8.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "aa": aa, "bb": bb, "cc": cc})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_8()
    return render(request, "math2sem/math2_4_8.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_9(request):
    global math_zad
    if request.POST:
        form = Math2_4_9(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                x, y, z = symbols('x,y,z')
                z = cd['z']
                g = cd['g']
                g = g.split("<=")
                u = sympify(z)
                g = g[1]
                g = int(g)
                kk1 = "-sqrt(bb-x**2)"
                kk1 = sympify(kk1)
                kk1 = kk1.subs({'bb': g})
                dd = u.subs({'y': kk1})
                ux = dd.diff(x)
                xx = solve(ux, x)
                yy = kk1.evalf(subs={'x': xx[0]})
                m1 = u.evalf(subs={'x': xx[0], 'y': yy})
                m2 = u.evalf(subs={'x': (xx[0] * -1), 'y': yy})
                m3 = u.evalf(subs={'x': xx[0], 'y': (yy * -1)})
                m4 = u.evalf(subs={'x': (xx[0] * -1), 'y': (yy * -1)})
                cont = min(m1, m2, m3, m4)
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_9.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_9()
    return render(request, "math2sem/math2_4_9.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_10(request):
    global math_zad
    if request.POST:
        form = Math2_4_10(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                x, y, z = symbols('x,y,z')
                z = cd['z']
                g = cd['g']
                g = g.split("<=")
                u = sympify(z)
                g = g[1]
                g = int(g)
                kk1 = "-sqrt(bb-x**2)"
                kk1 = sympify(kk1)
                kk1 = kk1.subs({'bb': g})
                dd = u.subs({'y': kk1})
                ux = dd.diff(x)
                xx = solve(ux, x)
                yy = kk1.evalf(subs={'x': xx[0]})
                m1 = u.evalf(subs={'x': xx[0], 'y': yy})
                m2 = u.evalf(subs={'x': (xx[0] * -1), 'y': yy})
                m3 = u.evalf(subs={'x': xx[0], 'y': (yy * -1)})
                m4 = u.evalf(subs={'x': (xx[0] * -1), 'y': (yy * -1)})
                cont = max(m1, m2, m3, m4)
                cont = floint(cont)
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_10.html",
                          {"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_10()
    return render(request, "math2sem/math2_4_10.html", {"form": form, "jj": jj, "math_zad": math_zad})


def math2_4_11(request):
    global math_zad
    if request.POST:
        form = Math2_4_11(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                a = cd['a']
                b = cd['b']
                c = cd['c']
                b /= 2
                dt = a * c - b ** 2
                if dt < 0:
                    cont = "в этой точке функция не имеет локального экстремума"
                elif dt == 0:
                    cont = "без дополнительных исследований нельзя сказать о наличии или отсутствии локального экстремума"
                elif dt > 0 and a > 0:
                    cont = "в этой точке функция имеет локальный минимум"
                elif dt > 0 and a < 0:
                    cont = "в этой точке функция имеет локальный максимум"
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except:
                cont = "Вы допустили ошибку при вводе формулы !!!"
            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            return render(request, "math2sem/math2_4_11.html",{"form": form, "jj": jj, "math_zad": math_zad, "cont": cont})
    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_11()
    return render(request, "math2sem/math2_4_11.html", {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math2_4_12(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                if a=="1":
                    aa="Параболы"
                elif a=="2":
                    aa="Пересекающиеся прямые"
                elif a=="3":
                    aa="Гиперболы"
                elif a=="4":
                    aa="Параллельные прямые"
                elif a=="5":
                    aa="Окружности"
                elif a=="6":
                    aa="Гиперболы"
                elif a=="7":
                    aa="Эллипсы"
                elif a=="8":
                    aa="Гиперболы"
                elif a=="9":
                    aa="Эллипсы"
                else:
                    raise IOError("Ошибка !!!")

                sss = {'Ответ': aa}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_12()
        return render(request, "math2sem/math2_4_12.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})


@csrf_exempt
def math2_4_13(request):
    global math_zad
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            try:
                if proverka(request.user) < math_zad:
                    jj = proverka(request.user)
                    raise IOError("У вас закончились пожертвования !!!")
                else:
                    pass
                a = request.POST['a']
                if a=="1":
                    aa="неограниченным, связным, замкнутым"
                elif a=="2":
                    aa="неограниченным, открытым, связным, областью"
                elif a=="3":
                    aa="ограниченным, связным, открытым, областью"
                elif a=="4":
                    aa="областью, неограниченным, открытым, связным"
                elif a=="5":
                    aa="замкнутым, неограничненным, несвязным"
                elif a=="6":
                    aa="замкнутым, ограниченным, связным"
                elif a=="7":
                    aa="неограниченным, замкнутым, "
                elif a=="8":
                    aa="неограниченным, областью, открытым, связным"
                elif a=="9":
                    aa="связным, ограниченным, областью, замкнутым"
                else:
                    raise IOError("Ошибка !!!")

                sss = {'Ответ': aa}
                moss = Money.objects.get(moneyname=request.user)
                moss.moneyvalue -= math_zad
                moss.save()
            except Exception as err:
                ff = str(err)
                sss = {'ff': ff}

            zzzzzzz = Money.objects.filter(moneyname=request.user)
            for fffffff in zzzzzzz:
                jj = fffffff.moneyvalue
            aa = str(request.user)
            return_object = {'obj': sss, 'obj2': jj, "math_zad": math_zad, "aa1": aa}
            return JsonResponse(return_object)
        else:
            global naeb
            sss = {'ff': naeb}
            return_object = {'obj': sss}
            return JsonResponse(return_object)

    else:
        zzzzzzz = Money.objects.filter(moneyname=request.user)
        for fffffff in zzzzzzz:
            jj = fffffff.moneyvalue
        form = Math2_4_13()
        return render(request, "math2sem/math2_4_13.html",
                      {"form": form, "jj": jj, "math_zad": math_zad})
