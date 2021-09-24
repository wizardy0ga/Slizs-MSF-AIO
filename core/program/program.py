from ..build.builder import payload
from ..build.builder import listener
from ..arguments.arguments import arguments
from ..graphics.graphics import graphics

graphics = graphics()
payload = payload()
listener = listener()
argument = arguments.args

class program:

    def launch(self):
        print(graphics.name)

        if argument.full:
            if argument.public:
                boolean = True
            else:
                boolean = False

            payload.createMSFpayload(argument.payload,argument.extension,argument.output,boolean,argument.interface)
            listener.multiHandler(argument.payload,argument.interface)

        else:
            listener.multiHandler(argument.payload,argument.interface)