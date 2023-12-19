import sys
import tensorflow as tf

from PIL import Image, ImageDraw, ImageFont
from transformers import AutoTokenizer, TFBertForMaskedLM

# Pre-trained masked language model
MODEL = "bert-base-uncased"

# Number of predictions to generate
K = 3

# Constants for generating attention diagrams
FONT = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 28)
GRID_SIZE = 40
PIXELS_PER_WORD = 200


def main():
    text = input("Text: ")

    # text = "She bought a [MASK] from the music store."

    # Tokenize input
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    inputs = tokenizer(text, return_tensors="tf")
    mask_token_index = get_mask_token_index(tokenizer.mask_token_id, inputs)
    if mask_token_index is None:
        sys.exit(f"Input must include mask token {tokenizer.mask_token}.")

    # Use model to process input
    model = TFBertForMaskedLM.from_pretrained(MODEL)
    result = model(**inputs, output_attentions=True)

    # Generate predictions
    mask_token_logits = result.logits[0, mask_token_index]
    top_tokens = tf.math.top_k(mask_token_logits, K).indices.numpy()
    for token in top_tokens:
        print(text.replace(tokenizer.mask_token, tokenizer.decode([token])))

    # Visualize attentions
    visualize_attentions(inputs.tokens(), result.attentions)


def get_mask_token_index(mask_token_id, inputs):
    """
    Return the index of the token with the specified `mask_token_id`, or
    `None` if not present in the `inputs`.

    inputs is a dictionary of tensors, "input_ids"
    """
    
    """
    CLS     The     San Diego   Chargers are  a      [MASK] football team .      SEP
    101     2624    5277        18649    2024 1037   103    2374     2136 1012   102 
    print(mask_token_id, inputs)
    103 
    {
        'input_ids': 
            <tf.Tensor: 
                shape=(1, 11), 
                dtype=int32, 
                numpy=array([[  101,  2624,  5277, 18649,  2024,  1037,   103,  2374,  2136, 1012, 102]], 
                dtype=int32)
            >, 
        'token_type_ids': 
            <tf.Tensor: 
                shape=(1, 11), 
                dtype=int32, 
                numpy=array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 
                dtype=int32)
            >, 
        'attention_mask': 
            <tf.Tensor: 
                shape=(1, 11), 
                dtype=int32, 
                numpy=array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], 
                dtype=int32)
            >
    }
    """
    # convert input_ids first ndarray to list to find index of mask token
    return list(inputs["input_ids"].numpy()[0]).index(mask_token_id)


def get_color_for_attention_score(attention_score):
    """
    Return a tuple of three integers representing a shade of gray for the
    given `attention_score`. Each value should be in the range [0, 255].

    San Diego Chargers are a professional football team.
    San Diego Chargers are a canadian football team.
    San Diego Chargers are a american football team.
    
    attention_score = tf.Tensor(0.04193281, shape=(), dtype=float32) 
    """
    # Tensors are a generic type that can have many values and types ...
    # Use keras backend to get the actual value
    score = tf.keras.backend.get_value(attention_score)
    # attention scores are between 0 and 1 inclusive, normalize
    # as a percentage of 255 (rgb max value)
    rgb_value = int(255 * score)

    # return same value for RGB in order to be a shade of gray
    return (rgb_value, rgb_value, rgb_value)


def visualize_attentions(tokens, attentions):
    """
    Produce a graphical representation of self-attention scores.

    For each attention layer, one diagram should be generated for each
    attention head in the layer. Each diagram should include the list of
    `tokens` in the sentence. The filename for each diagram should
    include both the layer number (starting count from 1) and head number
    (starting count from 1).

    <tf.Tensor: shape=(1, 12, 11, 11), dtype=float32, numpy=
    array([[[[ ... ]]]])

    https://www.tensorflow.org/guide/tensor for documentation on Tensor

    To index into the attentions value to get a specific attention head’s values, 
    you can do so as attentions[i][j][k], where 
        i is the index of the attention layer, 
        j is the index of the beam number (always 0 in our case), 
        k is the index of the attention head in the layer.

    In the base BERT model, the transformer uses 
        12 layers, where each layer has 
        12 self-attention heads, for a total of 144 self-attention heads.            
    """
    # TODO: Update this function to produce diagrams for all layers and heads.
    # print(attentions)
    for i in range(12):
        for k in range(12):
            # style50 suggests putting this on one line, but this
            # is more readable and follows the example provided.
            generate_diagram(
                i + 1,
                k + 1,
                tokens,
                attentions[i][0][k]
            )


def generate_diagram(layer_number, head_number, tokens, attention_weights):
    """
    Generate a diagram representing the self-attention scores for a single
    attention head. The diagram shows one row and column for each of the
    `tokens`, and cells are shaded based on `attention_weights`, with lighter
    cells corresponding to higher attention scores.

    The diagram is saved with a filename that includes both the `layer_number`
    and `head_number`.
    """
    # Create new image
    image_size = GRID_SIZE * len(tokens) + PIXELS_PER_WORD
    img = Image.new("RGBA", (image_size, image_size), "black")
    draw = ImageDraw.Draw(img)

    # Draw each token onto the image
    for i, token in enumerate(tokens):
        # Draw token columns
        token_image = Image.new("RGBA", (image_size, image_size), (0, 0, 0, 0))
        token_draw = ImageDraw.Draw(token_image)
        token_draw.text(
            (image_size - PIXELS_PER_WORD, PIXELS_PER_WORD + i * GRID_SIZE),
            token,
            fill="white",
            font=FONT
        )
        token_image = token_image.rotate(90)
        img.paste(token_image, mask=token_image)

        # Draw token rows
        _, _, width, _ = draw.textbbox((0, 0), token, font=FONT)
        draw.text(
            (PIXELS_PER_WORD - width, PIXELS_PER_WORD + i * GRID_SIZE),
            token,
            fill="white",
            font=FONT
        )

    # Draw each word
    for i in range(len(tokens)):
        y = PIXELS_PER_WORD + i * GRID_SIZE
        for j in range(len(tokens)):
            x = PIXELS_PER_WORD + j * GRID_SIZE
            color = get_color_for_attention_score(attention_weights[i][j])
            draw.rectangle((x, y, x + GRID_SIZE, y + GRID_SIZE), fill=color)

    # Save image
    img.save(f"Attention_Layer{layer_number}_Head{head_number}.png")


if __name__ == "__main__":
    main()
