Python bindings to the [`poktroll` client packages](https://pkg.go.dev/github.com/pokt-network/poktroll@v0.0.10/pkg/client).

## Clone `poktroll` and `poktroll-clients-py`
```bash
git clone https://github.com/bryanchriswhite/poktroll-clients-py
git clone https://github.com/byanchriswhite/poktroll --branch feat/client-cgo
```

## Build `poktroll` clients shared library & headers
```bash
cd poktroll

# Build shared library - NOTE: this will take a while until some import optimizations are done.
go build -o ../poktroll-clients-py/ext/libclients.so -buildmode=c-shared ./pkg/client/cgo_exports
cp ./pkg/client/cgo_exports/include/client.h ../poktroll-clients-py/ext/client.h

# Start poktroll localnet
make localnet_up
```

## Development environment setup
```bash
cd poktroll-clients-py

# Install dependencies
pip install pipenv
pipenv install
pipenv shell

# (optional) Update protobufs ("pull" from buf.build)
buf export buf.build/pokt-network/poktroll

# Generate protobufs
buf generate

# Run tests
pytest
```