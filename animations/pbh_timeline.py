import plotly.graph_objects as go


def create_pbh_timeline():

    stages = [

        "Big Bang",
        "Primordial\nDensity Fluctuations",
        "PBH\nFormation",
        "Slow\nHawking Evaporation",
        "Final\nExplosion",
        "Gamma-Ray\nBurst"
    ]

    x = [0, 1, 2, 3, 4, 5]
    y = [0] * len(x)

    colors = [
        "#FFD700",
        "#FFA500",
        "#7B68EE",
        "#00CED1",
        "#FF4500",
        "#FF0000"
    ]

    fig = go.Figure()

    # Timeline

    fig.add_trace(

        go.Scatter(

            x=x,

            y=y,

            mode="lines",

            line=dict(
                color="white",
                width=4
            ),

            hoverinfo="skip",

            showlegend=False

        )

    )

    # Stages

    fig.add_trace(

        go.Scatter(

            x=x,

            y=y,

            mode="markers+text",

            marker=dict(

                size=28,

                color=colors,

                line=dict(
                    color="white",
                    width=2
                )

            ),

            text=stages,

            textposition="top center",

            textfont=dict(size=13),

            showlegend=False

        )

    )

    fig.update_layout(

        paper_bgcolor="black",

        plot_bgcolor="black",

        font=dict(color="white"),

        xaxis=dict(

            visible=False,

            range=[-0.5,5.5]

        ),

        yaxis=dict(

            visible=False,

            range=[-1,1]

        ),

        height=350,

        margin=dict(

            l=20,

            r=20,

            t=30,

            b=20

        )

    )

    return fig
