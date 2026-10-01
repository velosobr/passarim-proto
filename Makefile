# Makefile — atalhos para os comandos do dia a dia.
# Uso: make generate | make lint | make breaking | make test

.PHONY: generate lint breaking test

# Gera o código Go a partir dos .proto.
generate:
	buf generate

# Verifica boas práticas nos .proto.
lint:
	buf lint

# Compara com a branch main e falha se houver mudança incompatível.
breaking:
	buf breaking --against '.git#branch=main'

# Roda os testes de contrato.
test:
	go test ./...
