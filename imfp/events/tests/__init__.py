from prezi.django_utils.tests import discover_tests


def suite():
    return discover_tests('imfp', __file__)
