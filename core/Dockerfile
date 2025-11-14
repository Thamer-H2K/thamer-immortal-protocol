# Thamer Immortal Protocol - Core Docker Image
# Copyright © 2025 Thamer-H2K. All Rights Reserved.

FROM rust:1.75-slim as builder

WORKDIR /build

COPY Cargo.toml ./

RUN mkdir src && \
    echo "fn main() {}" > src/main.rs && \
    cargo build --release && \
    rm -rf src

COPY src ./src

RUN cargo build --release

FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /build/target/release/thamer-core /app/thamer-core

RUN useradd -r -s /bin/false thamer
USER thamer

EXPOSE 8080

CMD ["/app/thamer-core"]