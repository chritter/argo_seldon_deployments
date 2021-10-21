# Custom SklearnServer Inference Server

Creates an image usable as a custom server.

* For custom inference servers one needs to modify a seldon config in the operator namespace. This is not practical if this kind of access is not possible as a user. There is an issue filed to allow for namespace-specific custom maps:
https://github.com/SeldonIO/seldon-core/issues/1674 
* Due to this restrictions I have not tested custom inference server.

## Reference

* https://docs.seldon.io/projects/seldon-core/en/stable/servers/custom.html


