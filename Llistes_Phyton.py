{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Llistes Phyton",
      "provenance": [],
      "authorship_tag": "ABX9TyPlUZMRoXGbTJAp8/1d+wvP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/FahadToqir/Python-ToqirFahad/blob/main/Llistes_Phyton.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f3fvyJnsOQNa",
        "outputId": "c049201f-1154-4e39-bca4-0731b6297cb3"
      },
      "source": [
        "x =(1,2,3,4,5,6)\n",
        "print (len(x))"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sxMuQKv-OOJ4",
        "outputId": "bfba7044-5680-4fe8-ffd5-12af8a784edc"
      },
      "source": [
        "x=(1,2,3,4,5,6)\n",
        "y=0\n",
        "while True:\n",
        "    print(x[y])\n",
        "    y+=1\n",
        "    if y == len(x):\n",
        "      break\n",
        "     "
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-fS2JAzKQqHw",
        "outputId": "1fbc9e74-6bd4-4c95-b64d-19e26d346cc4"
      },
      "source": [
        "x=(1,2,3,4,5,6)\n",
        "y=0\n",
        "while y < len(x):\n",
        "    print(x[y])\n",
        "    y+=1\n",
        "  "
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AI9fEpykRfWB",
        "outputId": "83bdb10a-6817-4eb1-bafb-423ec3234253"
      },
      "source": [
        "x=(1,2,3,4,5,6)\n",
        "y= len(x)-1\n",
        "z=0\n",
        "while z<=y:\n",
        "    print(x[z])\n",
        "    z+=1"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "77kbsHfQUHoH",
        "outputId": "72619bb4-6d36-4058-f7d5-a272a596245f"
      },
      "source": [
        "x=(1,2,3,4,5,6,7,8)\n",
        "y= len(x)-1\n",
        "while y>=0:\n",
        "    print(x[y])\n",
        "    y=y-1"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
