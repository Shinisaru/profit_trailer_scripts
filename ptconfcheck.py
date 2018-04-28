import argparse
import os.path

valid_parameters = {
    "pair_min_listed_days": 1,
    "orderbook_profit_calculation": 1,
    "consecutive_buy_trigger": 1,
    "consecutive_sell_trigger": 1,
    "price_trigger_market": 1,
    "price_rise_trigger": 1,
    "price_rise_recover_trigger": 1,
    "price_drop_trigger": 1,
    "price_drop_recover_trigger": 1,
    "start_balance": 1,
    "keep_balance": 1,
    "keep_balance_percentage": 1,
    "max_trading_pairs": 1,
    "market": 1,
    "enabled_pairs": 1,
    "hidden_pairs": 1,
    "*_dust": 1,
    "*_trading_enabled": 1,
    "*_DCA_enabled": 1,
    "*_initial_cost": 1,
    "*_initial_cost_percentage": 1,
    "*_min_buy_volume": 1,
    "*_min_buy_price": 1,
    "*_max_buy_spread": 1,
    "*_min_orderbook_volume_percentage": 1,
    "*_rebuy_timeout": 1,
    "*_buy_min_change_percentage": 1,
    "*_buy_max_change_percentage": 1,
    "*_*_buy_strategy": 1,
    "*_*_buy_value": 1,
    "*_*_buy_value_limit": 1,
    "*_*_buy_on_first_signal": 1,
    "*_*_sell_strategy": 1,
    "*_*_sell_value": 1,
    "*_trailing_buy": 1,
    "*_trailing_profit": 1,
    "*_max_profit": 1,
    "*_take_profit_percentage": 1,
    "*_take_profit_reset_percentage_move": 1,
    "*_take_profit_wait_time": 1,
    "*_pending_order_wait_time": 1,
    "*_combined_cancel_pending_trigger": 1,
    "*_stop_loss_trigger": 1,
    "*_stop_loss_timeout": 1,
    "*_panic_sell_enabled": 1,
    "*_sell_only_mode_enabled": 1,

    "DCA_keep_balance": 1,
    "DCA_keep_balance_percentage": 1,
    "SOM_DCA_buy_trigger": 1,
    "DCA_orderbook_profit_calculation": 1,
    "*_DCA_max_cost": 1,
    "*_DCA_max_buy_times": 1,
    "*_DCA_min_buy_volume": 1,
    "*_DCA_max_buy_spread": 1,
    "*_DCA_min_orderbook_volume_percentage": 1,
    "*_DCA_rebuy_timeout": 1,
    "*_DCA_buy_min_change_percentage": 1,
    "*_DCA_buy_max_change_percentage": 1,
    "*_DCA_ignore_sell_only_mode": 1,
    "*_DCA_*_buy_strategy": 1,
    "*_DCA_*_buy_value_1": 1,
    "*_DCA_*_buy_value_limit": 1,
    "*_DCA_buy_trigger": 1,
    "*_DCA_trailing_buy": 1,
    "*_DCA_buy_percentage": 1,
    "*_DCA_*_sell_strategy": 1,
    "*_DCA_*_sell_value": 1,
    "*_DCA_*_sell_value_*": 1,
    "*_DCA_trailing_profit": 1,
    "*_DCA_max_profit": 1,
    "*_DCA_take_profit_percentage": 1,
    "*_DCA_take_profit_reset_percentage_move": 1,
    "*_DCA_take_profit_wait_time": 1,
    "*_DCA_pending_order_wait_time": 1,
    "*_DCA_stop_loss_trigger": 1,
    "*_DCA_stop_loss_timeout": 1,

    "SOM_trigger_length": 1,
    "BB_std": 1,
    "BB_candle_period": 1,
    "BB_length": 1,
    "SMA_cross_candles": 1,
    "SMA_candle_period": 1,
    "SMA_fast_length": 1,
    "SMA_slow_length": 1,
    "EMA_cross_candles": 1,
    "EMA_candle_period": 1,
    "EMA_fast_length": 1,
    "EMA_slow_length": 1,
    "RSI_candle_period": 1,
    "RSI_length": 1,
    "STOCH_candle_period": 1,
    "STOCH_length": 1,
    "MACD_candle_period": 1,
    "MACD_fast_length": 1,
    "MACD_slow_length": 1,
    "MACD_signal": 1,
    "OBV_candle_period": 1,
    "OBV_length": 1,
    "OBV_signal": 1
}


def check(parameter_name):
    if parameter_name in valid_parameters:
        return True

    chunks = parameter_name.split("_")

    if len(chunks) > 0:
        chunks[0] = "*"
        if "_".join(chunks) in valid_parameters:
            return True

    if len(chunks) > 1:
        chunks[1] = "*"
        if "_".join(chunks) in valid_parameters:
            return True

    if len(chunks) > 2:
        chunks[1] = "DCA"
        chunks[2] = "*"
        if "_".join(chunks) in valid_parameters:
            return True

    return False


parser = argparse.ArgumentParser(description='Profit Trailer 2 configuration checker')
parser.add_argument('--file', dest='filename', action='store',
                    help='Path to profit trailer properties file')

args = parser.parse_args()

if args.filename is None or not os.path.isfile(args.filename):
    print("Provide properties file")
    exit(0)

with open(args.filename) as propf:
    for line in propf:
        line = line.strip()

        if len(line) == 0 or line[:1] == "#":
            continue

        param = line.split("=")
        if len(param) < 1:
            continue

        param = param[0].strip()
        if not check(param):
            print("Unknown parameter {0}".format(param))
