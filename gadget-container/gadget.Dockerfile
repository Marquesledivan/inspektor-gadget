# Builder: traceloop

# traceloop built from:
# https://github.com/kinvolk/traceloop/commit/20fdf3194e5ba62da0599443ebf24c28bd51bbb5
# See:
# - https://github.com/kinvolk/traceloop/actions
# - https://hub.docker.com/repository/docker/kinvolk/traceloop/tags

FROM docker.io/kinvolk/traceloop:2020051210515120fdf3 as traceloop

# Main gadget image

# BCC built from:
# https://github.com/kinvolk/bcc/commit/8de5fed9fb4b770d5dad483b6ab09df7e21fb6db
# See:
# - https://github.com/kinvolk/bcc/actions
# - https://hub.docker.com/repository/docker/kinvolk/bcc/tags

FROM docker.io/kinvolk/bcc:202005121923438de5fe

RUN set -ex; \
	export DEBIAN_FRONTEND=noninteractive; \
	apt-get update && \
	apt-get install -y --no-install-recommends \
		ca-certificates curl

COPY entrypoint.sh /entrypoint.sh
COPY cleanup.sh /cleanup.sh

COPY ocihookgadget/runc-hook-prestart.sh /bin/runc-hook-prestart.sh
COPY ocihookgadget/runc-hook-poststop.sh /bin/runc-hook-poststop.sh
COPY bin/ocihookgadget /bin/ocihookgadget

COPY bin/gadgettracermanager /bin/gadgettracermanager

COPY gadgets/bcck8s /opt/bcck8s
COPY bin/networkpolicyadvisor /bin/networkpolicyadvisor

COPY bin/runchooks.so /opt/runchooks/runchooks.so
COPY runchooks/add-hooks.jq /opt/runchooks/add-hooks.jq

COPY crio-hooks/gadget-prestart.json /opt/crio-hooks/gadget-prestart.json
COPY crio-hooks/gadget-poststop.json /opt/crio-hooks/gadget-poststop.json

COPY --from=traceloop /bin/traceloop /bin/traceloop
