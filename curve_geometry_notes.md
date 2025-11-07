# Differential Geometry of Curves

## Smooth Curves and Parameterizations
A smooth (regular) curve in $\mathbb{R}^3$ is a map $\gamma : I \rightarrow \mathbb{R}^3$ with $\gamma$ differentiable and $\dot{\gamma}(t) \neq 0$ for all $t$ in the interval $I$. Regularity ensures each point has a well-defined tangent vector $\mathbf{T}(t) = \dfrac{\dot{\gamma}(t)}{\lVert \dot{\gamma}(t) \rVert}$. When $\lVert \dot{\gamma}(t) \rVert = 1$ for all $t$, the parameter is the arc length $s$ and the curve is said to be parametrized by arc length.

## Curvature
Curvature measures how quickly the tangent direction changes along the curve. For an arc-length parametrized curve $\gamma(s)$, the curvature $\kappa(s)$ is
\[ \kappa(s) = \lVert \mathbf{T}'(s) \rVert. \
With a generic parameter $t$, use
\[ \kappa(t) = \frac{\lVert \dot{\gamma}(t) \times \ddot{\gamma}(t) \rVert}{\lVert \dot{\gamma}(t) \rVert^3}. \
Curvature is always non-negative; $\kappa = 0$ identifies straight lines, while larger $\kappa$ indicates tighter bending. For a plane circle of radius $R$, $\kappa = 1/R$ is constant.

## Principal Normal and Binormal
The principal normal vector is $\mathbf{N}(s) = \mathbf{T}'(s)/\kappa(s)$ when $\kappa \neq 0$. The binormal vector is $\mathbf{B}(s) = \mathbf{T}(s) \times \mathbf{N}(s)$. Together $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ form the Frenet frame, an orthonormal basis moving along the curve.

## Torsion
Torsion measures how the curve departs from being planar. For arc-length parameter:
\[ \tau(s) = -\mathbf{B}'(s) \cdot \mathbf{N}(s). \
In terms of any regular parameter $t$:
\[ \tau(t) = \frac{(\dot{\gamma}(t) \,\times\, \ddot{\gamma}(t)) \cdot \dddot{\gamma}(t)}{\lVert \dot{\gamma}(t) \times \ddot{\gamma}(t) \rVert^2}. \
Planar curves satisfy $\tau = 0$, while positive or negative torsion indicates the direction of twisting.

## Frenet--Serret Equations
For arc-length parametrized curves with nonzero curvature:
\[
\begin{aligned}
\mathbf{T}'(s) &= \kappa(s) \mathbf{N}(s), \\
\mathbf{N}'(s) &= -\kappa(s) \mathbf{T}(s) + \tau(s) \mathbf{B}(s), \\
\mathbf{B}'(s) &= -\tau(s) \mathbf{N}(s).
\end{aligned}
\]
These differential equations describe the evolution of the moving frame along the curve and encode its local geometry entirely through $\kappa$ and $\tau$.

## Examples
- **Helix** $\gamma(t) = (a\cos t, a\sin t, bt)$: curvature $\kappa = \dfrac{a}{a^2 + b^2}$ and torsion $\tau = \dfrac{b}{a^2 + b^2}$, both constant.
- **Cycloid** $\gamma(t) = (t - \sin t, 1 - \cos t)$: curvature $\kappa(t) = \dfrac{2}{(1 + \cos t)}$, which blows up at cusps.
- **Straight line**: $\kappa = 0$, torsion undefined but usually taken as $0$ since the Frenet frame collapses.

## Curvature of Plane Curves via Signed Curvature
For plane curves described by a function $y = y(x)$ with $y' = dy/dx$, the signed curvature is
\[ k(x) = \frac{y''}{(1 + (y')^2)^{3/2}}. \
The sign denotes orientation (left-turning or right-turning). For implicit curves $F(x,y)=0$, more general formulas involve gradients and Hessians.

## Practical Computation Tips
1. Reparameterize by arc length when possible to simplify formulas.
2. Normalize tangent vectors numerically before computing derivatives to improve stability.
3. When using discrete samples, approximate derivatives with finite differences and smooth the data to avoid noisy curvature estimates.
4. Verify planar curves by checking that the torsion numerically vanishes within tolerance.

These concepts form the backbone of curve design in computer graphics, robotics path planning, and the study of geodesics on surfaces.
