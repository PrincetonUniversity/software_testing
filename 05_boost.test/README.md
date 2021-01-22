# Boost.Test

Boost.Test is a popular framework for writing tests for C++ code.

## Della

See the documentation for [version 1.73](https://www.boost.org/doc/libs/1_73_0/libs/test/doc/html/index.html). Consider the following simple test (`test_file.cpp`):

```C++
#define BOOST_TEST_MODULE My Test
#include <boost/test/included/unit_test.hpp>

BOOST_AUTO_TEST_CASE(first_test)
{
  int i = 1;
  BOOST_TEST(i);
  BOOST_TEST(i == 2);
}
```

To compile and run the test:

```bash
$ module load boost/1.73.0
$ g++ test_file.cpp 
$ ./a.out 
Running 1 test case...
test_file.cpp(8): error: in "first_test": check i == 2 has failed [1 != 2]

*** 1 failure is detected in the test module "My Test" 
```

## Adroit

Adroit presently has only [version 1.53](https://www.boost.org/doc/libs/1_53_0/libs/test/doc/html/index.html) of the Boost libraries. If you want to write tests for C++ code on Adroit then request that the latest version of the Boost libraries be installed.
