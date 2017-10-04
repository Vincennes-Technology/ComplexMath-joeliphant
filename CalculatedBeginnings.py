#!/user/bin/python
# JOliphant
# Complex Beginnings
def complexAdding(a, b):
    realAnswers = a[0] + b[0]
    imagAnswers = a[1] + b[1]
    return (realAnswers, imagAnswers)

def complexSubtract(a, b):
    realAnswer = a[0] - b[0]
    imagAnswer = a[1] - b[1]
    return (realAnswer, imagAnswer)

def complexMultiplying(a, b):
    magnitudeAnswer = a[0] * b[0]
    phaseAnswer = a[1] + b[1]
    return (magnitudeAnswer, phaseAnswer)

def complexDividing(a, b):
    magnitudeAnswer = a[0] / b[0]
    phaseAnswer = a[1] - b[1]
    return (magnitudeAnswer, phaseAnswer)

print complexAdding((2,4),(2,6))
print complexSubtract((2,4),(2,6))
print complexMultiplying((2,4),(2,6))
print complexDividing((2,4),(2,6))
