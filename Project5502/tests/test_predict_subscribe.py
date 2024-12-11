import numpy as np
import math 
from production.functions import predict_subscribe

def test_make_predictions():
    # Given
    watch = -8.1
    duration = 1.4
    ctr = -0.7
    interest = 0
    misses = 0.32
    subscribes = 0.67
    
    # When
    result = predict_subscribe(watch, duration, ctr, interest)
    
    # Then
    assert isinstance(result, dict)
    assert isinstance(result["Misses Out"], np.float64)
    assert isinstance(result["Subscribes"], np.float64)
    assert math.isclose(result["Misses Out"], misses, abs_tol=0.01)
    assert math.isclose(result["Subscribes"], subscribes, abs_tol=0.01)