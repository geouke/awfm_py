from abc import ABC, abstractmethod

class AbstractAquiferDrawdownModel(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def model_drawdown_from_well(self, ts, x, y, pumping_well):
        pass

    @abstractmethod
    def normalize_units(self, factor_generator, units):
        pass

    def __str__(self):
        s = "BEGIN AquiferDrawdownModel\n"
        s += "  name: %s\n" %self.name()
        for param_name in self.params.keys():
            s += "%s: %s\n" %(param_name, str(self.params[param_name]))
        s += "END AquiferDrawdownModel"
        return s
