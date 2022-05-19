# global
import abc
from typing import Union, Optional

# local
import ivy

# ToDo: implement all methods here as public instance methods


class ArrayWithLinearAlgebra(abc.ABC):
    def matmul(
        self: ivy.Array,
        x2: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        out: Optional[Union[ivy.Array, ivy.NativeArray, ivy.Container]] = None,
    ) -> Union[ivy.Array, ivy.Container]:
        return ivy.matmul(self, x2, out=out)
    
   def inverse(self: ivy.Array, x2: Union[ivy.Array, ivy.NativeArray, ivy.Container], out: Optional[Union[ivy.Array, ivy.NativeArray, ivy.Container]] = None,
    ) -> Union[ivy.Array, ivy.Container]:
        x = np.array(x2)
        y = np.linalg.inv(x)
        return ivy.np.dot(x, y, out=out)
