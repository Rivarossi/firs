from cargo import Cargo

cargo = Cargo(id = 'passengers',
              number = '0',
              type_name = 'TTD_STR_CARGO_PLURAL_PASSENGERS',
              unit_name = 'TTD_STR_CARGO_SINGULAR_PASSENGER',
              type_abbreviation = 'TTD_STR_ABBREV_PASSENGERS',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '0.0625',
              station_list_colour = '152',
              cargo_payment_list_colour = '152',
              is_freight = '0',
              cargo_classes = 'bitmask(CC_PASSENGERS)',
              cargo_label = '"PASS"',
              town_growth_effect = 'TOWNGROWTH_PASSENGERS',
              town_growth_multiplier = '1.0',
              units_of_cargo = 'TTD_STR_PASSENGERS',
              items_of_cargo = 'TTD_STR_QUANTITY_PASSENGERS',
              penalty_lowerbound = '0',
              single_penalty_length = '22',
              capacity_multiplier = '4',
              price_factor = '101.749420166',
              icon_indices = (0, 0))
