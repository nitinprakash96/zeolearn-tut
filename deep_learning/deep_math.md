## Overview

About 3 months back I started exploring deep learning. I always thought it was a lot of matrices and their operations. I've never been more right! But digging more into the area and seeing the power it had, deep learning became one if the areas I like to work on now.

In this tutorial, I'll be walking you through the mathematics involved in Deep learning at the introductory level. Let's dive in!

## Liner Algebra. Really?

This basically revolved around Scalars, Vectors, Matrices and Tensors. Many people prefer avoiding this part of mathematics because it's not so fun to play with.

Let's see what the above mentioned are:

- #### Scalars
This is a simple number unlike other objects in linear algebra. In deep learning, scalars usually are represented by lower case variable names.

- #### Vectors
This is an array of numbers where each individual can be accessed by it's index. This is represented by a lowercase boldface variable name.

- #### Matrices
This is a 2D array of numbers and can be accessed by specifying two indices instead of one. This is represented by a Uppercase boldface variable name.

- #### Tensors
This might be fairly new to most of you. Sometimes to process the inputs we need an array that has more than two axes. Tensors, defined mathematically, are simply arrays of numbers, or functions, that transform according to certain rules under a change of coordinates.

There are a lot of operations applicable to the above objects that powers deep learning. Even though the objects above are boring, but rit's so pwerful that all of machine leanring, neural networks etc depend on it.

Let's see what are the operations that we can perform on these.

### Transpose

The `transpose` of a matrix is the mirror image of the matrix across the main diagonal, running down and to the right, starting from its upper left corner. We denote the transpose of a matrix A as A´ , and it is deﬁned such that A´(i,j) = A(j,i).

### Norm

Sometimes we need to measure the size of a vector. In machine learning, we usually measure the size of vectors using a function called a norm.  On an intuitive level, the norm of a vector x measures the distance from the origin to the point **x**. More rigorously, a norm is any function f that satisﬁes the following properties:

- f(**x**) = 0 => x = 0
- f (**x** + **y**) ≤ f(**x**) + f(**y**) (the triangle inequality)
- ∀α ∈ R, f(α**x** ) = |α|f(**x**)

### Eigen Decomposition

Many a times, there'll be a need when you will want to break a mathematical object into it's element so that you could understand it better and be able to process it. For example, an integer can be visualized as product of two or more integers.

Similarly, we can decompose matrices in ways that show us information about their functional properties. One of the most widely used kinds of matrix decomposition is called eigen-decomposition , in which we decompose a matrix into a set of eigenvectors and eigenvalues.

An eigenvector of a square matrix **A** is a non-zero vector **v** such that multiplication by **A** alters only the scale of **v**:

**Av** = **λv**

**λ** is an eigenvalue corresponding to this particular eigenvector. Okay, that'c cool. But what exactly this decomposition tells us? What is the significance?

Well, by doing eigen decomposition, we can conclude that:
- The matrix is singular if and only if eigen value is Zero.
- The eigen decomposition of a real symmetric matrix can also be used to optimize quadratic expressions of the form f( x ) = x ´ Ax subject to || x ||_2 = 1_.

### Singular Value Decomposition

This operation provides another way to factorize metrices. It breaks the matrix into singular values and Singular vectors.

The singular value decomposition is similar, except this time we will write A as a product of three matrices:

**A** = **UDV´**.

Here, </br>
**U** = m x m
**D** = m x n
**V** = n x n

Hence, **A** will be a m x n matrix.
The matrices **U** and **V** are both deﬁned to be orthogonal matrices. The matrix D is deﬁned to be a diagonal matrix. Note that D is not necessarily square. The elements along the diagonal of D are known as the singular values of the matrix A. The columns of U are known as the left-singular vectors. The columns of V are known as as the right-singular vectors.
