from cargo import Cargo

cargo = Cargo(id = 'iron_ore',
              number = '8',
              type_name = 'TTD_STR_CARGO_PLURAL_IRON_ORE',
              unit_name = 'TTD_STR_CARGO_SINGULAR_IRON_ORE',
              type_abbreviation = 'TTD_STR_ABBREV_IRON_ORE',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '181',
              cargo_payment_list_colour = '181',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_BULK)',
              cargo_label = '"IORE"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = 'TTD_STR_TONS',
              items_of_cargo = 'TTD_STR_QUANTITY_IRON_ORE',
              penalty_lowerbound = '30',
              single_penalty_length = '255',
              price_factor = '75.4852294922',
              capacity_multiplier = '1',
              icon_indices = (9, 0))

cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
cargo.economy_variations['MISTAH_KURTZ']['disabled'] = True