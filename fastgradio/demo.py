from gradio import Interface
from fastgradio.mappings import *
from fastai.learner import Learner


class Demo:
    """
    Demos are created with fastgradio by constructing a `fastgradio.Demo(learner)` object.
    """
    def __init__(self, learner):
        """
        :param learner: the fastai Learner object to wrap an interface around.
        """
        if isinstance(learner, Learner):
            self.learner = learner
            self.types = getattr(self.learner.dls, '_types')[tuple]
        else:
            raise ValueError(f"fastgradio only supports fastai.learner.Learner. Cannot create a demo from "
                             f"{type(learner)}.")

    def learner_predict(self, inp):
        """
        The function that will become the predict function inside `gradio.Interface`. It's constructed based on the
        processing in mappings.py
        :param inp:
        :return:
        """
        inp = mappings[self.types[0]]["process"](inp)
        prediction = self.learner.predict(inp)
        output = mappings[self.types[1]]["process"](self.learner.dls, prediction)
        return output

    def launch(self, share=True, debug=False, auth=None, **kwargs):
        """
        Launches the webserver that serves the UI for the interface.
        :param share: whether to create a publicly shareable link from your computer for the interface.
        :param debug: if True, and the interface was launched from Google Colab, prints the errors in the cell output.
        :param auth: If provided, username and password (or list of username-password tuples) required to access
        interface. Can also provide function that takes username and password and returns True if valid login.
        :param kwargs: everything that can be passed into `gradio.Interface()` except for fn, inputs, and outputs.
        Use this to pass in a title, description, examples, and more.
        :return:
        """
        try:
            inputs = mappings[self.types[0]]["type"]
        except KeyError:
            raise KeyError(f"fastgradio does not yet support {self.types[0]} as an input. Please use gradio "
                           f"instead and create your own fn, inputs and outputs.")
        try:
            outputs = mappings[self.types[1]]["type"]
        except KeyError:
            raise KeyError(f"fastgradio does not yet support {self.types[1]} as an output. Please use gradio "
                           f"instead and create your own fn, inputs and outputs.")
        Interface(fn=self.learner_predict, inputs=inputs, outputs=outputs,
                         **kwargs).launch(share=share, debug=debug, auth=auth)

