# Answer found in Q5 in Question Bank 1 (Tanet al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2780719051126377

    level1["cough"] = -1.0
    level1["cough_info_gain"] = -1.0

    level1["radon"] = -1.0
    level1["radon_info_gain"] = -1.0

    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = -1.0

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = -1.0
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = -1.0

    level2_left["radon"] = -1.0
    level2_left["radon_info_gain"] = 0.0

    level2_left["cough"] = 0.8812908992306927
    level2_left["cough_info_gain"] = 0.7219280948873623

    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = -1.0

    level2_right["radon"] = 0.7219280948873623
    level2_right["radon_info_gain"] = 0.7219280948873623

    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = -1.0

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = -1.0

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("smoking")  # MUST STILL CREATE THE TREE *****
    A = tree.insert_left("Chronic Cough")
    B = tree.insert_right("Radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    tree.print_tree()

    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.0

    # Infogain
    answer["(b) x < 0.2"] = 0.46438561897747244
    answer["(b) x < 0.7"] = 0.3602012209808308
    answer["(b) y < 0.6"] = 0.44217935649972373

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "x = 0.7"

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y = 0.7")
    tree.insert_left("x=0.7")
    tree.left.insert_left("B")
    tree.left.insert_right("y=0.3")
    tree.left.right.insert_left("A")
    tree.left.right.insert_right("C")

    tree.insert_right("x=0.2")
    tree.right.insert_left("y=0.8")
    tree.right.insert_right("A")
    tree.right.left.insert_left("C")
    tree.right.left.insert_right("B")
    tree.print_tree()
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.5
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.4914

    answer["(f) attr for splitting"] = "Car Type"

    # Explanatory text string
    answer["(f) explain choice"] = "I will choose Car Type as the splitting attribute at the root node because it has the lowest Gini index among the three attributes."

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ["binary", "qualitative", "nominal"]

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "AM and PM are categories with no inherent order"

    answer["b"] = ["continuous", "quantitative", "ratio"]
    answer["b: explain"] = "Brightness can vary infinitely and has a meaningful zero point."

    answer["c"] = ["continuous", "qualitative", "ordinal"]
    answer["c: explain"] = "Continuous or discrete, depending on how judgments are recorded. If recorded on a continuous scale, it would be continuous and quantitative, ordinal. If recorded as categories (e.g., dim, moderate, bright), it would be discrete and qualitative, ordinal."

    answer["d"] = ["Continuous", "quantitative", "ratio"]
    answer["d: explain"] = "Angles can take any value within the specified range and have a meaningful zero point."

    answer["e"] = ["discrete", "qualitative", "nominal"]
    answer["e: explain"] = "Bronze, Silver, Gold are categories with no inherent order."

    answer["f"] = ["continuous", "quantitative", "ratio"]
    answer["f: explain"] = "Height can vary infinitely and has a meaningful zero point."

    answer["g"] = ["discrete", "quantitative", "ratio"]
    answer["g: explain"] = "The number of patients is a whole number count with no meaningful fractions."

    answer["h"] = ["discrete", "qualitative", "nominal"]
    answer["h: explain"] = "ISBN numbers are unique identifiers for books but do not convey any inherent order or quantity."

    answer["i"] = ["discrete", "qualitative", "ordinal"]
    answer["i: explain"] = "These are categories with an inherent order from least to most light passing ability."

    answer["j"] = ["discrete","qualitative", "ordinal"]
    answer["j: explain"] = "Military ranks have a hierarchical order."

    answer["k"] = ["continuous", "quantitative", "ratio"]
    answer["k: explain"] = "Distance can vary infinitely and has a meaningful zero point."

    answer["l"] = ["continuous", "quantitative", "ratio"]
    answer["l: explain"] = "Density can vary infinitely and has a meaningful zero point."

    answer["m"] = ["discrete", "quantitative", "nominal"]
    answer["m: explain"] = "The Check numbers are unique identifiers for coats with no inherent order."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Because of its higher testing accuracy, Model 2 manages unseen data better. Given how much greater the training accuracy is than the testing accuracy, Model 1 appears to be overfitted."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "The measures provided are just the averages of the two datasets' accuracies. Both the models have been trained on Dataset A, so they will always get them right, but Model 2 still has a higher accuracy when it comes to Dataset B, the real unseen data."

    explain["c similarity"] = "Incorporation of Model Complexity"
    explain["c similarity explain"] = "The goal of both pessimistic error estimate techniques and MDL is to penalize decision tree complexity. Assuming that simpler models generalize better to unseen data, they seek to strike a compromise between the tree's size or complexity and its ability to match the training data."

    explain["c difference"] = "Approach to Model Complexity"
    explain["c difference explain"] = "The MDL Principle calls for a trade-off between the model's complexity—which is determined by how long the description must be in order to capture the model—and how well the model fits the data. On the other hand, the Pessimistic Error Estimate directly alters a decision tree's error estimate by including a penalty term that rises in complexity with the tree (for instance, the number of leaf nodes)."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x <= 0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y <= 0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "x <= 0.2"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.58

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x <= 0.5")

    A = tree.insert_right("A")
    B = tree.insert_left("y <= 0.4")
    B.insert_left("A")
    B.insert_right("x <= 0.2")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 0.0
    answer["b, info gain, Handedness"] = -1.474

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "Based on the information gain, Handedness should not be chosen as the splitting attribute because it results in negative information gain. So we will choose the ID attribute"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.0
    answer["e, gain ratio, Handedness"] = -0.737

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Based"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

