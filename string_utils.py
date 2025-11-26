def split_before_each_uppercases(formula):
    if formula == "":
        return []
    start = 0
    end = 1
    split_formula = []
    for i in formula[1:]:
      if i.isupper():
          split_formula.append(formula[start:end])
          start = end
          end = start + 1

      else:
        end += 1
    split_formula.append(formula[start:end])
    return (split_formula)


def split_at_first_digit(formula):
    digit_location = 1
    for i in formula[1:]:
      if i.isdigit():
        break

      else:
        digit_location += 1

    prefix = formula[:digit_location]
    num_pos = formula[digit_location:]

    if digit_location == len(formula):
        return (formula, 1)

    return (prefix, int(num_pos))

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    molecule_dict = {}
    parts = split_before_each_uppercases(molecular_formula) # returns a list of the formula alike : (H2, HM, Mh3)
    for i in parts:
      element, amount = split_at_first_digit(i)
      molecule_dict[element] = molecule_dict.get(element, 0) + amount
    return molecule_dict



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
