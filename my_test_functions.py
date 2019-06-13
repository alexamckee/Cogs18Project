from my_module.my_functions import remove_punctuation

def test_remove_punctuation():
    test_string= 'g/!ood'
    removed= remove_punctuation(test_string)
    
    assert removed== 'good'
    
test_remove_punctuation()