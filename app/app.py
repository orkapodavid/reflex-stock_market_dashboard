import reflex as rx

from app.components.line_chart import trading_line_chart
from app.components.main_header import main_header
from app.components.options_table import options_table
from app.components.orders_table import orders_table
from app.components.positions_table import positions_table
from app.states.trading_state import TradingState


def index() -> rx.Component:
    """The main page component for the trading dashboard."""
    return rx.el.div(
        main_header(),
        rx.el.main(
            trading_line_chart(),
            options_table(),
            orders_table(),
            positions_table(),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-4 p-4",
        ),
        class_name="min-h-screen bg-gray-900 text-gray-300 font-sans",
        on_mount=TradingState.start_simulation,
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/styles.css"],
)
app.add_page(index, route="/")
