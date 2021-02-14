import os
import sys
import unittest

sys.path.insert(0, os.getcwd())

from pynewtonmath import core, wrapper


class TestWrapper (unittest.TestCase):
    def test_expose_endpoints (self):
        for op in core.ENDPOINTS:
            self.assertTrue(op in dir(wrapper))
            print('.', end='', flush=True)
    
    
    def test_endpoints (self):
        # operation: (expression, result)
        tests = {
            'simplify': ('x^2 + 2x', 'x^2 + 2 x'),
            'factor': ('x^2 + 2x', 'x (x + 2)'),
            'derive': ('x^2+2x', '2 x + 2'),
            'integrate': ('x^2+2x', '1/3 x^3 + x^2'), # + C missing
            'zeroes': ('x^2+2x', [-2, 0]),
            'tangent': ('2|x^3', '12 x + -16'),
            'area': ('2:4|x^3', 60),
            'cos': ('pi', -1),
            'sin': ('0', 0),
            'tan': ('0', 0),
            'arccos': ('1', 0),
            'arcsin': ('0', 0),
            'arctan': ('0', 0),
            'abs': ('-1', 1),
            'log': ('2|8', 3),
        }
        
        for op, test in tests.items():
            exp, result = test
            self.assertEqual(getattr(wrapper, op)(exp), result)
            print('.', end='', flush=True)
    
    
    def test_extended_endpoints (self):
        self.assertEqual(wrapper.tangent('x^3', 2), '12 x + -16')
        self.assertEqual(wrapper.area('x^3', 2, 4), 60)
        self.assertEqual(wrapper.log(8, 2), 3)

__help__ = """
 Here is the help for the Math module:

Solves complex math problems using https://newton.now.sh
 - /simplify: Simplify /simplify 2^2+2(2)
 - /factor: Factor /factor x^2 + 2x
 - /derive: Derive /derive x^2+2x
 - /integrate: Integrate /integrate x^2+2x
 - /zeroes: Find 0's /zeroes x^2+2x
 - /tangent: Find Tangent /tangent 2lx^3
 - /area: Area Under Curve /area 2:4lx^3
 - /cos: Cosine /cos pi
 - /sin: Sine /sin 0
 - /tan: Tangent /tan 0
 - /arccos: Inverse Cosine /arccos 1
 - /arcsin: Inverse Sine /arcsin 0
 - /arctan: Inverse Tangent /arctan 0
 - /abs: Absolute Value /abs -1
 - /log: Logarithm /log 2l8
Keep in mind: To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).
"""

__mod_name__ = "MATHS"

SIMPLIFY_HANDLER = DisableAbleCommandHandler("simplify", simplify)
FACTOR_HANDLER = DisableAbleCommandHandler("factor", factor)
DERIVE_HANDLER = DisableAbleCommandHandler("derive", toss)
INTEGRATE_HANDLER = DisableAbleCommandHandler("integrate", integrate)
ZEROES_HANDLER = DisableAbleCommandHandler("zeroes", zeroes)
TANGENT_HANDLER = DisableAbleCommandHandler("tangent", tangent)
AREA_HANDLER = DisableAbleCommandHandler("area", area)
COS_HANDLER = DisableAbleCommandHandler("cos", cos)
SIN_HANDLER = DisableAbleCommandHandler("sin", sin)
TAN_HANDLER = DisableAbleCommandHandler("tan", tan)
ARCCOS_HANDLER = DisableAbleCommandHandler("arccos", arccos)
ARCSIN_HANDLER = DisableAbleCommandHandler("arcsin", arcsin)
ARCTAN_HANDLER = DisableAbleCommandHandler("arctan", arctan)
ABS_HANDLER = DisableAbleCommandHandler("abs", abs)
LOG_HANDLER = DisableAbleCommandHandler("log", log)

dispatcher.add_handler(SIMPLIFY_HANDLER)
dispatcher.add_handler(FACTOR_HANDLER)
dispatcher.add_handler(DERIVE_HANDLER)
dispatcher.add_handler(INTEGRATE_HANDLER)
dispatcher.add_handler(ZEROES_HANDLER)
dispatcher.add_handler(TANGENT_HANDLER)
dispatcher.add_handler(AREA_HANDLER)
dispatcher.add_handler(COS_HANDLER)
dispatcher.add_handler(SIN_HANDLER)
dispatcher.add_handler(TAN_HANDLER)
dispatcher.add_handler(ARCCOS_HANDLER)
dispatcher.add_handler(ARCSIN_HANDLER)
dispatcher.add_handler(ARCTAN_HANDLER)
dispatcher.add_handler(ABS_HANDLER)
dispatcher.add_handler(LOG_HANDLER)

if __name__ == '_main_':
    unittest.main()