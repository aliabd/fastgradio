import gradio
from mappings import mappings
import fastai


class Demo:
    def __init__(self, predict_fn):
        if isinstance(predict_fn, fastai.learner.Learner):
            self.learner = predict_fn
            self.types = getattr(self.learner.dls, '_types')[tuple]
        else:
            raise ValueError(f"fast-gradio only supports fastai.learner.Learner. Cannot create a demo from "
                             f"{type(predict_fn)}.")

    def learner_predict(self, inp):
        inp = mappings[self.types[0]]["process"](inp)
        prediction = self.learner.predict(inp)
        output = mappings[self.types[1]]["process"](self.learner.dls, prediction)
        return output

    def launch(self, share=True, **kwargs):
        gradio.Interface(fn=self.learner_predict, inputs=mappings[self.types[0]]["type"], outputs=mappings[
            self.types[1]]["type"], **kwargs).launch(share=share)

