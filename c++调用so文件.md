在C++中调用Python函数（特别是来自Cython生成的shared object）需要涉及到Python C API。以下是如何从C++中调用`passport_processing_v1.cpython-310-x86_64-linux-gnu.so`中的`process_passport_image`函数的基本步骤：

1. **包含必要的头文件**:

```
#include <Python.h>
```

1. **初始化Python解释器**:

```
Py_Initialize();
```

1. **导入模块**:

```
PyObject *pName = PyUnicode_DecodeFSDefault("passport_processing_v1");
PyObject *pModule = PyImport_Import(pName);
Py_DECREF(pName);
```

1. **获取函数并调用它**:

```
if (pModule != NULL) {
    PyObject *pFunc = PyObject_GetAttrString(pModule, "process_passport_image");
    
    if (PyCallable_Check(pFunc)) {
        PyObject *pArgs = PyTuple_Pack(1, PyUnicode_FromString("your_input_data_here"));
        PyObject *pValue = PyObject_CallObject(pFunc, pArgs);
        
        // ... 处理返回的pValue ...

        Py_DECREF(pValue);
        Py_DECREF(pArgs);
    } else {
        PyErr_Print();
    }
    Py_XDECREF(pFunc);
    Py_DECREF(pModule);
} else {
    PyErr_Print();
}
```

1. **结束Python解释器**:

```
Py_Finalize();
```

1. **编译**: 当编译C++代码时，确保链接到Python库，并确保Python头文件和`.so`文件在您的include和library路径中。例如，使用g++:

```
g++ your_cpp_file.cpp -o output -I/usr/include/python3.10 -L/path/to/your/so/file -lpython3.10 -lpassport_processing_v1
```

**注意**:

- 这里的代码只是一个简化的示例，您可能需要根据您的具体需求进行修改。
- 请确保Python版本与您在C++代码中使用的版本相匹配。
- 调用Python C API需要小心，尤其是关于引用计数和错误处理。如果不正确地进行，可能会导致内存泄漏或其他问题。
- 还要确保您的C++程序能够找到Python运行时环境和任何依赖的Python模块或包。

最后，尽管使用Python C API从C++中调用Python函数是可行的，但在实际的生产环境中，这可能会引入额外的复杂性和潜在的问题。如果可以，尽量避免这种混合编程，或者考虑使用其他桥接技术，如[Boost.Python](https://www.boost.org/doc/libs/1_77_0/libs/python/doc/html/index.html)。