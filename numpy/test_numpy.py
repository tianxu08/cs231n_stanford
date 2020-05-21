import numpy as np

def numpy_array_1():
    a = np.array([[1.0, 2.0], [3.0, 4.0]]) 
    b = np.array([[5.0, 6.0], [7.0, 8.0]]) 
    sum = a + b 
    difference = a - b 
    product = a * b   # element-wise multiply
    quotient = a / b  # element-wise divide
    print("a = \n" + str(a))
    print("b = \n" + str(b))
    print ("Sum = \n" +  str(sum))
    print ("Difference = \n" + str(difference))
    print ("Product = \n"+ str(product))
    print ("Quotient = \n" + str(quotient))
    
    matrix_product = a.dot(b)
    print("Matrix_product = \n" + str(matrix_product))
 
def numpy_create_array():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array((0, 1, 2, 3, 4))
    c = np.arange(5)
    d = np.linspace(0, 2*np.pi, 2)  
    #numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
    
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    print("d = " + str(d))

def numpy_2d_array():
    a = np.array(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
            [26, 27, 28 ,29, 30],
            [31, 32, 33, 34, 35],
            [36, 37, 38 ,39, 40],
        ])
    # print(a)
    # print(a.shape)
    # a_3d = a.reshape(2, 2, 10)
    # print(a_3d)
    # print(a_3d.shape)
    # print("-------------------")
    # a_4d = a.reshape(2, 2, 2, 5)
    # print(a_4d)
    # print(a_4d.shape)
    
    b = np.arange(120)
    print(b.shape)
    b_4d = b.reshape(2, 3, 4, 5)
    # print(b_4d.shape)
    # print(b_4d)

    print(b.dtype)
    print(b.size)
    print(b_4d.ndim)

def numpy_mulitple():
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])
    
    v = np.array([9, 10])
    w = np.array([11, 12])
    print(x * y)
    print(np.multiply(x, y))
    
    print('--------------')
    # Inner product of vectors; both produce 219
    print(v.dot(w))
    print(np.dot(v, w))
    print('##############')
    # Matrix / vector product; both produce the rank 1 array [29 67]
    print(x.dot(v))
    print(np.dot(x, v))
    print('$$$$$$$$$$$$$$')
    # Matrix / matrix product; both produce the rank 2 array
    # [[19 22]
    #  [43 50]]
    print(x.dot(y))
    print(np.dot(x, y))
    
def numpy_sum():
    x = np.array([[1,2],[3,4]])
    print(x)
    print(np.sum(x))  # Compute sum of all elements; prints "10"
    print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
    print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

def numpy_matrix_t():
    
    x = np.array([[1,2], [3,4], [5, 6]])
    print(x)
    print(x.T)

def numpy_broadcast():
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([10, 100, 1000])
    # w = np.array([[10], [100], [1000]])
    y = x + v
    # print(x)
    # print(v)
    # print(y)
    
    v = np.array([1, 2, 3])
    w = np.array([4, 5])
    
    print(np.reshape(v, (3, 1)) * w)
    x = np.array([[1,2,3], [4,5,6]])
    

if __name__ == "__main__":
    # numpy_array_1()
    # numpy_create_array()
    # numpy_2d_array()
    # numpy_mulitple()
    # numpy_sum()
    # numpy_matrix_t()
    numpy_broadcast()
    