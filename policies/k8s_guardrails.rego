package kubernetes.admission

import rego.v1

# Rule 1: Deny containers running as root (Security Compliance)
deny contains msg if {
    input.kind == "Deployment"
    some container in input.spec.template.spec.containers
    not container.securityContext.runAsNonRoot
    msg := sprintf("SECURITY VIOLATION: Container '%v' must set securityContext.runAsNonRoot = true", [container.name])
}

# Rule 2: Deny containers without FinOps memory limits (Cost Governance)
deny contains msg if {
    input.kind == "Deployment"
    some container in input.spec.template.spec.containers
    not container.resources.limits.memory
    msg := sprintf("FINOPS VIOLATION: Container '%v' must define resources.limits.memory", [container.name])
}
