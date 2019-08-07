#!/usr/bin/env python3.7

import iterm2
import subprocess

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Kubernetes context",
        detailed_description="Indicates current kubernetes context",
        knobs=[],
        exemplar="dev-hzo",
        update_cadence=5,
        identifier="com.iterm2.status-bar.kubectx")

    @iterm2.StatusBarRPC
    async def coro(knobs):
        value = subprocess.check_output([ '/usr/local/bin/kubectl', 'config', 'current-context' ]).decode().strip()

        return "k8s: " + value

    await component.async_register(connection, coro, timeout=None)

iterm2.run_forever(main)
