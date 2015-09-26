
class FeatureExtractor(object):

    def __init__(self):
        pass

    def transform(self, temperatures_xray, n_burn_in, n_lookahead, skf_is):
        """Compute the single variable of mean temperatures in the El Nino 3.4 
        region."""
        # This is the range for which features should be provided. Strip
        # the burn-in from the beginning and the prediction look-ahead from
        # the end.
        valid_range = range(n_burn_in, temperatures_xray['time'].shape[0] - n_lookahead)
        enso = get_enso_mean(temperatures_xray['tas'])
        enso_valid = enso.values[valid_range]
        X = enso_valid.reshape((enso_valid.shape[0], 1))
        # trying to cheat by looking ahead
        return X
