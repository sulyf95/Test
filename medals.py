medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

medalPoints = {
    1: 3,
    2: 2,
    3: 1,
}

def createMedalTable(results):
    medalTable = {}
    for position in results:
        for country in position["podium"]:
            pfd = country.split(".")

            pfd_standing = pfd[0]
            pfd_country = pfd[1]

            if pfd_country in medalTable:
                medalTable[pfd_country] += medalPoints[int(pfd_standing)]
            else:
                medalTable[pfd_country] = medalPoints[int(pfd_standing)]

    df_ordered = sorted(medalTable.items(), key=lambda x: x[1], reverse=True)
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    return(medalTable)

def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable

