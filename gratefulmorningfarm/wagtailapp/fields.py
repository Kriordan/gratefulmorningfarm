from wagtail.core.blocks import Block
from wagtail.core.fields import StreamField

from gratefulmorningfarm.wagtailapp.blocks import ComponentStreamBlock


class ComponentStreamField(StreamField):
    def __init__(self, block_types, **kwargs):
        super().__init__(block_types, **kwargs)
        if not isinstance(block_types, Block) and not isinstance(
            block_types, type
        ):  # other cases already handled by super call
            self.stream_block = ComponentStreamBlock(
                block_types, required=not self.blank
            )
