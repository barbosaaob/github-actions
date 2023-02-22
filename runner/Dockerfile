FROM ubuntu:22.04

WORKDIR /actions-runner

RUN apt-get update && apt-get upgrade -y && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Create and switch to runner user
RUN useradd -s /usr/bin/bash runner && chown -R runner /actions-runner
USER runner

# Runner Download
ARG ARCH=x64
ARG VERSION=2.301.1
RUN curl -o actions-runner-linux-$ARCH-$VERSION.tar.gz -L https://github.com/actions/runner/releases/download/v$VERSION/actions-runner-linux-$ARCH-$VERSION.tar.gz && tar xzf ./actions-runner-linux-$ARCH-$VERSION.tar.gz && rm ./actions-runner-linux-$ARCH-$VERSION.tar.gz

# Switch back to root to install dependencies
USER root
RUN ./bin/installdependencies.sh && rm -rf /var/lib/apt/lists/*

# Runner Configuration
USER runner
ARG TOKEN
ARG REPO_URL
ARG RUNNER_GROUP=Default
ARG NAME=7eb93bb9bff8
ARG LABELS='self-hosted,Linux,X64'
ARG WORK=_work
RUN ./config.sh --url $REPO_URL --token $TOKEN --runnergroup $RUNNER_GROUP --name $NAME --labels $LABELS --work $WORK

ENTRYPOINT ["./run.sh"]
