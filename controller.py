from flask import Flask, jsonify, request

def getModulo():
    return jsonify({'response': 'modulo'})