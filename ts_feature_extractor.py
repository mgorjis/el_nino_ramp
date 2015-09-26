class FeatureExtractor(object):
    def __init__(self):
        pass

    def fit(self, temperatures_xray, n_burn_in, n_lookahead):
        pass

    def transform(self, temperatures_xray, n_burn_in, n_lookahead, skf_is):
        """Use world temps as features."""
        # Set all temps on world map as features
        all_temps = temperatures_xray['tas'].values
        time_steps, lats, lons = all_temps.shape
        all_temps = all_temps.reshape((time_steps, lats * lons))
        all_temps = all_temps[n_burn_in:-n_lookahead, :]
        return all_temps
