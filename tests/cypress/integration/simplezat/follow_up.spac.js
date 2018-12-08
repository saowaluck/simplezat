
context('Rating', () => {
  beforeEach(() => {
    cy.visit('https://localhost:8000')
  })


  it('should have 3 rating', () => {
    cy.contains('How do we do')
    cy.get('img').should('have.attr', 'alt', 'Positive')
    cy.get('img').should('have.attr', 'alt', 'Netual')
    cy.get('img').should('have.attr', 'alt', 'Negative')

    cy.get('img["Positive"]').click()

    cy.contains('Any comment?')
    cy.get('inputp[name="comment"]').type('You are doing great!')
    cy.get('button').click()

    cy.contains('Thank you')
  })
})
