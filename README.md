# [Clean Architectures in Python](https://leanpub.com/clean-architectures-in-python)

- [Demo Implementation Repo](https://github.com/pycabook/rentomatic)
- [파이썬으로 구현하는 클린 아키텍처](https://dailyheumsi.tistory.com/240)
- [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [The Testing Pyramid: How to Structure Your Test Suite](https://semaphoreci.com/blog/testing-pyramid)
- [Test Pyramid Tutorial: Comprehensive Guide With Best Practices](https://www.lambdatest.com/learning-hub/test-pyramid)

## Install Dependencies

```bash
pip install -r requirements/dev.txt
```

## Unit Test

```bash
pytest -svv
```

## Integration Test

```bash
./manage.py test -- --integration
```

## Build a Docker Image

```bash
./manage.py compose build web
```

## Compose Up

```bash
./manage.py compose up -d
```

## Compose Down

```bash
./manage.py compose down
```
