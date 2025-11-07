"""Plot a circle with Plotly."""
import numpy as np
import plotly.graph_objects as go

def plot_circle(radius=1.0, center=(0.0, 0.0), samples=400):
    theta = np.linspace(0.0, 2.0 * np.pi, samples)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    fig = go.Figure(
        data=[go.Scatter(x=x, y=y, mode="lines", name="circle")]
    )
    fig.update_layout(
        title=f"Circle (r={radius}, center={center})",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y", scaleratio=1.0, zeroline=True),
        yaxis=dict(constrain="domain", zeroline=True),
        template="plotly_white",
        height=600,
        width=600,
    )
    fig.show()

if __name__ == "__main__":
    plot_circle()
