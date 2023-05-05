# Arvigo ML Model

> This ML model would come in hand in detecting human faces and non-human objects.

## Development

### Dependencies

```
tensorflow-estimator==2.12.0
tensorflow-macos==2.12.0
tensorflow-metal==0.8.0
numpy==1.23.0
keras==2.12.0
Werkzeug==2.3.3
```

If you're on macOS, you can use `tensorflow_macos==2.12.0`

### How to run

```
flask --app saulius run
```

### How to run with live reload

```
flask --app debug --debug run
```


## Usage

Endpoint for detecting:

```
URL: 127.0.0.1:5000/is_human
Method: POST
Body: image="base64stringhere"
```

In HTTPie, we can write this as: `http POST "127.0.0.1:5000/is_human" image="base64stringhere" `