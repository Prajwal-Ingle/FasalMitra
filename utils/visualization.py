"""
FasalMitra AI - Modern Agricultural Data Visualizations (Plotly)
"""
from typing import Dict, List, Any
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from config import COLORS

PLOTLY_LAYOUT_TEMPLATE = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(20, 39, 28, 0.4)",
    font=dict(family="system-ui, -apple-system, sans-serif", color=COLORS["text_primary"], size=12),
    margin=dict(l=40, r=30, t=40, b=40),
    xaxis=dict(
        gridcolor="#284A36",
        zerolinecolor="#284A36",
        tickfont=dict(color=COLORS["text_secondary"]),
        title_font=dict(color=COLORS["text_primary"], size=13)
    ),
    yaxis=dict(
        gridcolor="#284A36",
        zerolinecolor="#284A36",
        tickfont=dict(color=COLORS["text_secondary"]),
        title_font=dict(color=COLORS["text_primary"], size=13)
    ),
    legend=dict(
        font=dict(color=COLORS["text_primary"]),
        bgcolor="rgba(13, 31, 21, 0.8)",
        bordercolor="#284A36",
        borderwidth=1
    )
)


def create_pest_bar_chart(class_counts: Dict[str, int]) -> go.Figure:
    """Creates a sleek bar chart of detected pest frequencies."""
    if not class_counts:
        fig = go.Figure()
        fig.add_annotation(
            text="No pests detected in current view",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=14, color=COLORS["text_secondary"])
        )
        fig.update_layout(**PLOTLY_LAYOUT_TEMPLATE, height=280)
        return fig

    df = pd.DataFrame(list(class_counts.items()), columns=["Pest", "Count"])
    df = df.sort_values(by="Count", ascending=True)

    fig = go.Figure(go.Bar(
        x=df["Count"],
        y=df["Pest"],
        orientation="h",
        marker=dict(
            color=COLORS["accent_emerald"],
            line=dict(color="#10B981", width=1)
        ),
        text=df["Count"],
        textposition="auto",
        textfont=dict(color="#0D1F15", size=12, family="ui-monospace")
    ))

    fig.update_layout(
        **PLOTLY_LAYOUT_TEMPLATE,
        title=dict(text="<b>Detected Species Distribution</b>", font=dict(size=14, color=COLORS["text_primary"])),
        xaxis_title="Specimen Count",
        yaxis_title="",
        height=max(260, len(df) * 35),
    )
    return fig


def create_confidence_histogram(confidences: List[float]) -> go.Figure:
    """Creates a clean confidence distribution chart."""
    if not confidences:
        fig = go.Figure()
        fig.add_annotation(
            text="No confidence data available",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=14, color=COLORS["text_secondary"])
        )
        fig.update_layout(**PLOTLY_LAYOUT_TEMPLATE, height=280)
        return fig

    pcts = [round(c * 100, 1) for c in confidences]
    
    fig = go.Figure(go.Histogram(
        x=pcts,
        nbinsx=10,
        marker=dict(
            color=COLORS["accent_amber"],
            line=dict(color="#D97706", width=1)
        ),
        opacity=0.85
    ))

    fig.update_layout(
        **PLOTLY_LAYOUT_TEMPLATE,
        title=dict(text="<b>Model Confidence Spread (%)</b>", font=dict(size=14, color=COLORS["text_primary"])),
        xaxis_title="Confidence Percentage (%)",
        yaxis_title="Detections",
        height=280
    )
    return fig


def create_crop_distribution_pie(history_records: List[Dict[str, Any]]) -> go.Figure:
    """Creates a donut chart representing scans per crop context."""
    crops = [r.get("crop", "Unknown") for r in history_records if r.get("crop")]
    if not crops:
        fig = go.Figure()
        fig.add_annotation(
            text="No session history data",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=14, color=COLORS["text_secondary"])
        )
        fig.update_layout(**PLOTLY_LAYOUT_TEMPLATE, height=300)
        return fig

    counts = pd.Series(crops).value_counts().reset_index()
    counts.columns = ["Crop", "Scans"]

    palette = [
        COLORS["accent_emerald"], COLORS["accent_gold"], "#60A5FA",
        "#F87171", "#A78BFA", "#38BDF8", "#4ADE80", "#FB923C"
    ]

    fig = go.Figure(go.Pie(
        labels=counts["Crop"],
        values=counts["Scans"],
        hole=0.55,
        marker=dict(colors=palette, line=dict(color="#14271C", width=2)),
        textinfo="label+percent",
        textfont=dict(size=12, color=COLORS["text_primary"])
    ))

    fig.update_layout(
        **PLOTLY_LAYOUT_TEMPLATE,
        title=dict(text="<b>Scans by Crop Category</b>", font=dict(size=14, color=COLORS["text_primary"])),
        height=320,
        showlegend=False
    )
    return fig


def create_session_timeline_chart(history_records: List[Dict[str, Any]]) -> go.Figure:
    """Creates a line/scatter chart showing detection counts across session sequence."""
    if not history_records:
        fig = go.Figure()
        fig.add_annotation(
            text="No scans performed in this session yet",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=14, color=COLORS["text_secondary"])
        )
        fig.update_layout(**PLOTLY_LAYOUT_TEMPLATE, height=280)
        return fig

    indices = [f"Scan #{i+1}" for i in range(len(history_records))]
    pests = [r.get("num_detections", 0) for r in history_records]
    latencies = [r.get("inference_time_ms", 0.0) for r in history_records]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=indices,
        y=pests,
        name="Pests Detected",
        marker=dict(color=COLORS["accent_emerald"]),
        yaxis="y"
    ))

    fig.add_trace(go.Scatter(
        x=indices,
        y=latencies,
        name="Latency (ms)",
        mode="lines+markers",
        line=dict(color=COLORS["accent_amber"], width=2),
        yaxis="y2"
    ))

    layout = dict(**PLOTLY_LAYOUT_TEMPLATE)
    layout["yaxis2"] = dict(
        title="Latency (ms)",
        overlaying="y",
        side="right",
        gridcolor="rgba(0,0,0,0)",
        tickfont=dict(color=COLORS["accent_amber"]),
        title_font=dict(color=COLORS["accent_amber"])
    )
    layout["title"] = dict(text="<b>Session Detection Activity & Performance</b>", font=dict(size=14))
    layout["height"] = 300

    fig.update_layout(layout)
    return fig
