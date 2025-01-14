//
//   this typemap is used together with %extend, which
//   adds a class member taking int *pymfem_size 
//
%define ARRAY_LISTTUPLE_INPUT(XXX, YYY)  
 %typemap(in) (void *List_or_Tuple, XXX *_unused ) (
				    XXX *temp_ptr,
				    int size,
     				    bool is_tuple=false){
  if (!PyList_Check($input)) {
      if (!PyTuple_Check($input)) {
         PyErr_SetString(PyExc_ValueError, "Expecting a list/tuple");
         return NULL;
      } else {
	is_tuple = true;
      }
  }
  size = (is_tuple) ? PyTuple_Size($input) : PyList_Size($input);
  $1 = (void *) & size;
}

%typemap(argout) (void *List_or_Tuple, XXX *_unused ) {
  for (int i = 0; i < size$argnum; i++) {
      PyObject *s = (is_tuple$argnum) ? PyTuple_GetItem($input, i) : PyList_GetItem($input,i);
      (* result)[i] =  (XXX)YYY(s);
  }
}
  
%typemap(typecheck) (void *List_or_Tuple, XXX *_unused ) {
  $1 = 0;
  if (PyList_Check($input)){
    $1 = 1;
  }
  if (PyTuple_Check($input)){
    $1 = 1;
  }
}
%enddef

%define ARRAY_LISTTUPLE_INPUT_SWIGOBJ(XXX, USEPTR)
 %typemap(in) (void *List_or_Tuple, XXX *_unused ) (
				    int size,
     				    bool is_tuple=false){
  if (!PyList_Check($input)) {
      if (!PyTuple_Check($input)) {
         PyErr_SetString(PyExc_ValueError, "Expecting a list/tuple");
         return NULL;
      } else {
	is_tuple = true;
      }
  }
  size = (is_tuple) ? PyTuple_Size($input) : PyList_Size($input);
  $1 = (void *) & size;
}

%typemap(argout) (void *List_or_Tuple, XXX *_unused ) {
  //PyObject *name = PyUnicode_FromString("__setitem__");
  
  #if USEPTR == 1
  XXX  temp_ptr$argnum;
  swig_type_info *ty = $descriptor(const XXX);
  #else
  XXX * temp_ptr$argnum;
  swig_type_info *ty = $descriptor(const XXX *);
  #endif

  for (int i = 0; i < size$argnum; i++) {
      PyObject *s = (is_tuple$argnum) ? PyTuple_GetItem($input, i) : PyList_GetItem($input,i);
      if (!SWIG_IsOK(SWIG_ConvertPtr(s, (void **) &temp_ptr$argnum, ty, 0|0))) {
   	  PyErr_SetString(PyExc_ValueError, "List items must be XXX");
      } else {
	  #if USEPTR==1
          (* result)[i] =  temp_ptr$argnum;
	  #else
          (* result)[i] =  *temp_ptr$argnum;
	  #endif
      }
  }
}
  
%typemap(typecheck) (void *List_or_Tuple, XXX *_unused ) {
  $1 = 0;
  if (PyList_Check($input)){
    $1 = 1;
  }
  if (PyTuple_Check($input)){
    $1 = 1;
  }
}
%enddef

