Family Tree CLI
---
A CLI based application for the creating family tree

## Define a family tree:

`family-tree add-person <name>`
eg: family-tree add-person Amit Dhakad

`family-tree add-relationship <name>`
eg: family-tree add-relationship father
eg: family-tree add-relationship son

`family-tree connect <name 1> as <relationship> of <name 2>`
eg: family-tree connect "Amit Dhakad" as son of "KK Dhakad"

## Queries:

Based on relations created, we should be able to make following queries
`family-tree count sons of <name>`
This should count sons

`family-tree count daughters of <name>`
This should count of all daughters

`family-tree count wives of <name>`
This should count wives

`family-tree father of <name>`
This should return father name