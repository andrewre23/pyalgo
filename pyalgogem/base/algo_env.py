#
# PyAlgo Project
# base/
#
#
# Andrew Edmonds - 2018
#

import pyalgogem.data as data
import pyalgogem.backtest as backtest
import pyalgogem.deployment as deployment
import pyalgogem.performance as performance


class AlgorithmEnvironment(object):
    """
    Main class for Gemini wrapper and interactive tool

    """

    def __init__(self, key, secret_key, sandbox=True, debug=False):
        """
        Creates algorithm_environment object (ae)

        Parameters
        ==========
        key: string
            Gemini API key
        secret_key: string
            Gemini secret API key
        sandbox: bool
            set to using sandbox account or live account
        debug: bool
            if true, print requests and function outputs

        Attributes
        ==========
        filename: str
            name of datafile to be used by environment
        instrument: str
            name of instrument to be used - must be BTC or ETH

        """
        # add pathways to other subfolders
        self.data = data
        self.backtest = backtest
        self.deployment = deployment
        self.performance = performance

        # set parametric values
        self.key = key
        self.secret_key = secret_key
        if sandbox:
            self.url = 'https://api.sandbox.gemini.com/v1/'
        else:
            self.url = 'https://api.gemini.com/v1/'
        self.debug = debug

        # set initial attributes
        self.filename = 'data.h5'
        self.instrument = None

        # create datafile if none exists
        self.data.create_datafile(self.filename)

    def set_instrument(self, instrument):
        """Update instrument to be used in algorithm"""
        if instrument.upper() not in ['BTC', 'ETH']:
            raise ValueError("Instrument must be BTC or ETH")
        else:
            self.instrument = instrument.upper()

    def set_datafile(self, filename):
        filename = str(filename)
        self.filename = self.data.create_datafile(filename)
