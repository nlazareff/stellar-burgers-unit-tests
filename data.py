class TestDataReceipt:
    RECEIPT_TEST_DATA = [
        ([], [
            "(==== test_bun ====)",
            "(==== test_bun ====)",
            "",
            "Price: 2000.0"
        ]),
        (['mock_filling'], [
            "(==== test_bun ====)",
            "= filling test_filling =",
            "(==== test_bun ====)",
            "",
            "Price: 2500.0"
        ]),
        (['mock_sauce'], [
            "(==== test_bun ====)",
            "= sauce test_sauce =",
            "(==== test_bun ====)",
            "",
            "Price: 2050.0"
        ]),
        (['mock_filling', 'mock_sauce'], [
            "(==== test_bun ====)",
            "= filling test_filling =",
            "= sauce test_sauce =",
            "(==== test_bun ====)",
            "",
            "Price: 2550.0"
        ])
    ]
