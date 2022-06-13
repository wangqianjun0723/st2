__defaults__(
    all=dict(
        resolve="pylint_plugins",
    )
)

python_sources()

python_tests(
    name="tests",
    dependencies=[
        "!//conftest.py:root",
    ],
)

python_requirement(
    name="pylint",
    requirements=[
        # This must be the same as [pylint].version in pants.toml
        "pylint~=2.8.2",
        # other requirements in [pylint].extra_requirements in pants.toml
        "setuptools",
    ],
)

python_requirement_library(
    name="astroid",
    # The version of astroid is constrained by the pylint version above
    requirements=["astroid"],
)
