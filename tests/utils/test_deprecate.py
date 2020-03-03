import unittest
from importlib import import_module
from discretize import TensorMesh
mesh = TensorMesh([2,2,2])

deprecated_modules = [
    'SimPEG.utils.codeutils',
    'SimPEG.utils.coordutils',
    'SimPEG.utils.CounterUtils',
    'SimPEG.utils.curvutils',
    'SimPEG.utils.matutils',
    'SimPEG.utils.meshutils',
    'SimPEG.utils.ModelBuilder',
    'SimPEG.utils.PlotUtils',
    'SimPEG.utils.SolverUtils',
    'SimPEG.electromagnetics.utils.EMUtils',
    'SimPEG.electromagnetics.utils.AnalyticUtils',
    'SimPEG.electromagnetics.utils.CurrentUtils',
    'SimPEG.electromagnetics.utils.testingUtils',
    'SimPEG.electromagnetics.static.utils.StaticUtils',
]

deprecated_problems = [
    ['SimPEG.electromagnetics.frequency_domain',
        ('Problem3D_e', 'Problem3D_b', 'Problem3D_h', 'Problem3D_j')],
    ['SimPEG.electromagnetics.time_domain',
        ('Problem3D_e', 'Problem3D_b', 'Problem3D_h', 'Problem3D_j')],
    ['SimPEG.electromagnetics.natural_source',
        ('Problem3D_ePrimSec', 'Problem1D_ePrimSec')],
    ['SimPEG.electromagnetics.static.induced_polarization',
        ('Problem3D_CC', 'Problem3D_N', 'Problem2D_CC', 'Problem2D_N')],
    ['SimPEG.electromagnetics.static.resistivity',
        ('Problem3D_CC', 'Problem3D_N', 'Problem2D_CC', 'Problem2D_N')],
    ['SimPEG.electromagnetics.static.spectral_induced_polarization',
        ('Problem3D_CC', 'Problem3D_N', 'Problem2D_CC', 'Problem2D_N')],
    ['SimPEG.electromagnetics.viscous_remanent_magnetization',
        ('Problem_Linear', 'Problem_LogUnifrom')],
]

class DeprecateTest(unittest.TestCase):

    def test_module_deprecations(self):
        for module in deprecated_modules:
            print(module, end='...')
            with self.assertWarns(DeprecationWarning):
                import_module(module)
            print('ok')

    def test_problem_deprecations(self):
        for module in deprecated_problems:
            mod = import_module(module[0])
            for Problem in module[1]:
                Prob = getattr(mod, Problem)
                print(f'{module[0]}.{Problem}...', end='')
                with self.assertWarns(DeprecationWarning):
                    Prob(mesh=mesh)
                print('ok')

if __name__ == '__main__':
    unittest.main()