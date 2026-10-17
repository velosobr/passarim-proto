# passarim-proto

Contratos gRPC do **Passarim** — o app das aves do Brasil.
Este repositório é a **fonte da verdade** de como o BFF conversa com a Catalog API.

## Onde ele se encaixa

```mermaid
flowchart LR
    BFF[passarim-bff<br/>cliente gRPC] -- usa código gerado --> P[(passarim-proto)]
    CAT[passarim-catalog<br/>servidor gRPC] -- usa código gerado --> P
    BFF -- gRPC: ListSpecies / GetSpecies / ListFilters --> CAT
```

## Por que um repositório só para contratos?
Se o contrato vivesse dentro do catalog, o BFF dependeria do código do catalog.
Separando, os dois dependem apenas de um acordo comum e versionado.
Ver [ADR-003](https://github.com/velosobr/passarim-docs/blob/main/docs/adr/0003-grpc-interno-rest-externo.md).

## Comandos
| Comando | O que faz |
|---|---|
| `make lint` | Verifica boas práticas nos `.proto` |
| `make generate` | Gera o código Go em `gen/go` |
| `make breaking` | Falha se houver mudança incompatível com a `main` |
| `make test` | Testes de contrato |

## Como usar em outro serviço
```bash
go get github.com/velosobr/passarim-proto@latest
```
```go
import catalogv1 "github.com/velosobr/passarim-proto/gen/go/passarim/catalog/v1"
```

## Serviços

| Arquivo | Serviço | Quem implementa | Quem chama |
|---|---|---|---|
| `proto/passarim/catalog/v1/catalog.proto` | `CatalogService` | passarim-catalog | passarim-bff |
| `proto/passarim/curator/v1/curator.proto` | `PhotoCuratorService` | passarim-photo-curator | worker do passarim-catalog |

## Código gerado

- Go: `gen/go` (módulo `github.com/velosobr/passarim-proto`).
- Python: `gen/python`, instalável como pacote (ver `gen/python/README.md`).

Os dois são gerados com `buf generate` e versionados; a CI falha se estiverem desatualizados.
