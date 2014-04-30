"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "0. Basics": [
        {
            "input": ["Programming", "Gram Ring Mop"],
            "answer": True,
        },
        {
            "input": ["Hello", "Ole Ho"],
            "answer": False,
        },

        {
            "input": ["Kyoto", "Tokyo"],
            "answer": True,
        }

    ],
    "1. Extra": [
        {
            "input": ["Hamlet", "Amleth"],
            "answer": True,
        },
        {
            "input": ["Kings Lead Hat", "Talking Heads"],
            "answer": True,
        },
        {
            "input": ["abcdefghijklmnopqrstuvwxyz", "Cwm fjord bank glyphs vext quiz"],
            "answer": True,
        },
        {
            "input": ["Listen", "Silent"],
            "answer": True,
        },
        {
            "input": ["A telephone girl", "Repeating allo"],
            "answer": False,
        },
        {
            "input": ["Waitress", "The stew Sir"],
            "answer": False,
        },
        {
            "input": ["The Morse Code", "There Come Dots"],
            "answer": False,
        },

    ],
    "2. Edge": [
        {
            "input": ["a", "a"],
            "answer": True,
        },
        {
            "input": ["x", "X"],
            "answer": True,
        },
        {
            "input": ["A O X", "x o a"],
            "answer": True,
        },
        {
            "input": ["  Hi  all  ", "all hi"],
            "answer": True,
        },
        {
            "input": ["a", "z"],
            "answer": False,
        },
        {
            "input": ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU",
                      'UTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'],
            "answer": True,
        },
        {
            "input": ["bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU",
                      'TSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'],
            "answer": False,
        },
        {
            "input": ["aaaaaaaaabbb", "ba"],
            "answer": False,
        },
    ]
}
