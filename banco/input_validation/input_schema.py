from jsonschema import validate


schema = {
    "title": "Schematic for Input Model",
    "type": "object",
    "required": ["start_date", "end_date", "client"],
    "properties":{
        "start_date":{
            "type": "number"
        },
        "end_date":{
            "type": "number"
        },
        "client":{
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "address": {"$ref": "#/$defs/address"},
                    "contact": {"$ref": "#/$defs/contact"},
                    "cpf": {
                        "type": "integer",
                        "minimum": 0
                    },
                    "documents": {"$ref": "#/$defs/documents"},
                    "parent_name": {"$ref": "#/$defs/parent_name"},
                    "income_type": {
                        "type": "string"
                    },
                    "birthday": {
                        "type": "string"
                    },
                    "register_date": {
                        "type": "integer"
                    }
                },
            },
        },
    },
    "$defs": {
        "address": {
            "title": "Adress",
            "type": "object",
            "required": ["street", "number", "neighborhood", "city", "State", "postal_code"],
            "properties": {
                "street": {
                    "type": "string"
                },
                "number": {
                    "type": "string"
                },
                "neighborhood": {
                    "type": "string"
                },
                "city": {
                    "type": "string"
                },
                "state": {
                    "type": "string"
                },
                "postal_code": {
                    "type": "string"
                }
            }
        },
        "contact": {
            "title": "Contact",
            "type": "object",
            "required": ["phone", "email"],
            "properties": {
                "phone":{
                    "type": "integer"
                },
                "email": {
                    "type": "string"
                }
            }
        },
        "documents": {
            "title": "Documents",
            "type": "object",
            "required": ["identity", "passport", "driver_license"],
            "properties": {
                "identity":{
                    "type": "string"
                },
                "passport": {
                    "type": ["string", "null"]
                },
                "driver_license": {
                    "type": ["string", "null"]
                }
            }
        },
        "parent_name": {
            "title": "Parent Name",
            "type": "object",
            "required": ["mother", "father"],
            "properties": {
                "mother":{
                    "type": "string"
                },
                "father": {
                    "type": ["string", "null"]
                }
            }
        },
    }
}
