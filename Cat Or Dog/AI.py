import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# dataset loading ( our AI's information )
data_gen = ImageDataGenerator(rescale=1./255)
train_data = data_gen.flow_from_directory(directory='data',
                                           target_size=(224,224),
                                           class_mode='binary',
                                           batch_size=32)
val_data = data_gen.flow_from_directory(directory='data',
                                         target_size=(224,224),
                                         class_mode='binary',
                                         batch_size=32)

# create the model ( AI )
model = keras.Sequential([
    keras.Input(shape=(224, 224, 3)),
    layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# compile the model ( AI )
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# train the model ( AI )
history = model.fit(
    train_data, 
    epochs=10, 
    steps_per_epoch = 100,
    validation_data=val_data,
    validation_steps = 50)

model.save('models')